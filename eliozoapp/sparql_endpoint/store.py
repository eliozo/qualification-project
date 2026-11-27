"""A read-only store handle that follows data reloads.

The ``load_rdf`` Jenkins pipeline deletes the store directory and builds a
new one while this service keeps running. A read-only RocksDB handle never
notices: it keeps serving the deleted files (Linux keeps them alive while
they are open) and sees a frozen snapshot of the data as of opening time.

``StoreHolder`` therefore checks, at most every ``check_interval`` seconds, a
cheap fingerprint of the store directory (its inode, the manifest that
``CURRENT`` names, that manifest's size and mtime). When the fingerprint has
changed, the store is reopened once

* no process holds the writer lock on ``LOCK`` (Linux only), and
* no file in the store directory was modified in the last ``settle`` seconds.

The check runs on requests, so an idle worker picks up a finished reload on
its first request after it.

Until then the old handle keeps answering with the old data, so a reload
causes no downtime. If reopening fails, the old handle is kept too.
"""

import logging
import os
import struct
import sys
import threading
import time

from pyoxigraph import Store

log = logging.getLogger(__name__)

try:
    import fcntl
except ImportError:  # Windows
    fcntl = None

# struct flock on Linux (x86_64 and aarch64): l_type, l_whence, l_start,
# l_len, l_pid. Other systems lay it out differently, so the lock probe is
# Linux-only; elsewhere only the settle time protects against a running load.
_FLOCK = 'hhqqi4x'


class StoreUnavailable(Exception):
    """The store directory is missing or cannot be opened."""


def writer_active(store_path):
    """True when another process holds the RocksDB writer lock of the store."""
    if fcntl is None or not sys.platform.startswith('linux'):
        return False
    try:
        fd = os.open(os.path.join(store_path, 'LOCK'), os.O_RDONLY)
    except OSError:
        return False
    try:
        probe = struct.pack(_FLOCK, fcntl.F_WRLCK, 0, 0, 0, 0)
        lockType = struct.unpack(_FLOCK, fcntl.fcntl(fd, fcntl.F_GETLK, probe))[0]
        return lockType != fcntl.F_UNLCK
    except OSError:
        return False
    finally:
        os.close(fd)


def fingerprint(store_path):
    """A tuple that changes whenever the store is rebuilt or written; None if absent."""
    try:
        st = os.stat(store_path)
        with open(os.path.join(store_path, 'CURRENT'), encoding='ascii') as f:
            manifest = f.read().strip()
        mst = os.stat(os.path.join(store_path, manifest))
    except (OSError, ValueError):
        return None
    return (st.st_dev, st.st_ino, manifest, mst.st_size, mst.st_mtime_ns)


def last_modified(store_path):
    """The newest mtime (seconds) of the files in the store directory; 0 if unreadable."""
    newest = 0.0
    try:
        with os.scandir(store_path) as entries:
            for entry in entries:
                try:
                    newest = max(newest, entry.stat().st_mtime)
                except OSError:
                    pass
    except OSError:
        pass
    return newest


class StoreHolder:
    def __init__(self, store_path, check_interval=2.0, settle=5.0,
                 opener=Store.read_only, clock=time.monotonic, wallclock=time.time):
        self.store_path = store_path
        self.check_interval = check_interval
        self.settle = settle
        self._opener = opener
        self._clock = clock
        self._wallclock = wallclock
        self._lock = threading.Lock()
        self._store = None
        self._fingerprint = None
        self._last_check = None
        self.generation = 0           # incremented on every (re)open
        self.opened_at = None         # wall-clock time of the last (re)open

    def get(self):
        """The current store; reopens it first when a finished reload is detected."""
        with self._lock:
            now = self._clock()
            if self._store is None:
                self._open(fingerprint(self.store_path))
            elif self._last_check is None or now - self._last_check >= self.check_interval:
                self._last_check = now
                self._maybe_reopen()
            return self._store

    def _open(self, fp):
        if not os.path.isdir(self.store_path):
            raise StoreUnavailable(f'store not found at {self.store_path}')
        try:
            store = self._opener(self.store_path)
        except OSError as e:
            raise StoreUnavailable(str(e))
        self._store, self._fingerprint = store, fp
        self._last_check = self._clock()
        self.generation += 1
        self.opened_at = self._wallclock()
        log.info('opened store %s (generation %d)', self.store_path, self.generation)

    def _maybe_reopen(self):
        fp = fingerprint(self.store_path)
        if fp is None or fp == self._fingerprint:
            return          # missing (mid-reload: keep serving the old data) or unchanged
        if self._wallclock() - last_modified(self.store_path) < self.settle:
            return          # still being written
        if writer_active(self.store_path):
            return
        old = self._store
        try:
            self._open(fp)
        except StoreUnavailable as e:
            log.warning('reopening the store failed, keeping the old handle: %s', e)
            return
        del old

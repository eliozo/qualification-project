"""Page navigation shared by the Filter page and the search results.

Templates render it with the ``page_bar`` macro from ``_paging.html``. Page
size and the page bar length limit are set in ``eliozo_dao.problem_listing``.
"""

from flask import url_for

from eliozo_dao.problem_listing import PAGE_BAR_LIMIT, PAGE_SIZE


def parse_offset(value):
    """The ``offset`` request argument as a non-negative int; 0 if absent or invalid."""
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def page_offsets(total, page_size=PAGE_SIZE):
    """Offsets of all result pages, e.g. ``total=23`` gives ``[0, 10, 20]``.

    Empty when everything fits on one page, so no page bar is shown.
    """
    if total <= page_size:
        return []
    return list(range(0, total, page_size))


def shown_page_numbers(page_count, current, limit=PAGE_BAR_LIMIT):
    """Page numbers to put in the page bar.

    Up to ``limit`` pages all are shown. Beyond that: the first and the last
    page and two pages on each side of ``current``; a single left-out page is
    shown instead of being replaced by an ellipsis.
    """
    if page_count <= limit:
        return list(range(1, page_count + 1))
    shown = {1, page_count}
    shown.update(n for n in range(current - 2, current + 3) if 1 <= n <= page_count)
    for n in sorted(shown):
        if n + 2 in shown and n + 1 not in shown:
            shown.add(n + 1)
    return sorted(shown)


def page_links(total, current_offset, endpoint, params, page_size=PAGE_SIZE, limit=PAGE_BAR_LIMIT):
    """Items of the page bar.

    One ``{'number', 'url', 'current'}`` dict per shown page, and ``{'gap': True}``
    where page numbers are left out. ``params`` are the query parameters every
    page link repeats; the ``offset`` parameter is added last.
    """
    offsets = page_offsets(total, page_size)
    if not offsets:
        return []
    items = []
    previous = 0
    for number in shown_page_numbers(len(offsets), current_offset // page_size + 1, limit):
        if number > previous + 1:
            items.append({'gap': True})
        offset = (number - 1) * page_size
        items.append({'number': number,
                      'url': url_for(endpoint, **params, offset=offset),
                      'current': offset == current_offset})
        previous = number
    return items

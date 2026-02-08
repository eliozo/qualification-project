
import platform
import os

FUSEKI_URL_LINUX = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
os_name = platform.system()

if os_name == 'Windows':
    FUSEKI_URL = FUSEKI_URL_LINUX
else:
    FUSEKI_URL = FUSEKI_URL_LINUX

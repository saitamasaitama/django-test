from http.client import HTTPConnection
import urllib.request


def req():
    url = 'https://example.com/api/v1/resource'
    data = {
        'foo': 123,
    }
    headers = {
        'Content-Type': 'application/json',
    }

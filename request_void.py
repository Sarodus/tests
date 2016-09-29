import socket
import urlparse
import urllib
from collections import namedtuple


class RequestVoid:

    """Sends a request, no response, no wait."""

    URL_PARAMS = namedtuple('URL_PARAMS', 'host port path query')

    @staticmethod
    def _send(url_params, headers):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((url_params.host, url_params.port))
        s.send(headers)
        s.close()

    @staticmethod
    def _get_url_params(url, params):
        parsed_url = urlparse.urlparse(url)

        query = urllib.urlencode(params)
        path = parsed_url.path or '/'
        if query:
            path += '?' + query

        return RequestVoid.URL_PARAMS(
            host=parsed_url.hostname,
            port=parsed_url.port or 80,
            path=path,
            query=query
        )

    @staticmethod
    def get(url, params={}):
        url_params = RequestVoid._get_url_params(url, params)

        headers = (
            'GET %s HTTP/1.1\r\n'
            '\r\n'
        ) % url_params.path

        RequestVoid._send(url_params, headers)

    @staticmethod
    def post(url, params={}, data={}):
        url_params = RequestVoid._get_url_params(url, params)
        form = urllib.urlencode(data)

        headers = (
            'POST %s HTTP/1.1\r\n'
            'Content-Length: %s\r\n'
            'Content-Type: application/x-www-form-urlencoded\r\n'
            '\r\n'
            '%s'
        ) % (url_params.path, len(form), form)

        RequestVoid._send(url_params, headers)

if __name__ == '__main__':
    url = 'http://example.com/'
    RequestVoid.get(url)

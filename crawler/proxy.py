"""
Proxy module allowing fetchers to use proxy servers.
"""


class Proxy(object):
    """
    List of free UK proxy is here https://free-proxy-list.net/uk-proxy.html
    """
    def __init__(self, ip, port=80):
        self.ip = ip
        self.port = port

    @property
    def uri(self):
        return f'http://{self.ip}:{self.port}/'

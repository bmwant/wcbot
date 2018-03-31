"""
Grab information needed from a resource and store it.
"""
from utils import get_logger


class Grabber(object):
    def __init__(self, base_url, requester=None, parser=None, cache=None):
        name = self.__class__.__name__.lower()
        self.base_url = base_url
        self.requester = requester
        self.parser = parser
        self.cache = cache
        self.logger = get_logger(name)

    def __await__(self):
        return self.requester.request(self.base_url)

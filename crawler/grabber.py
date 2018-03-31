"""
Grab information needed from a resource and store it.
"""
from utils import get_logger


class Grabber(object):
    def __init__(self, name, requester=None, parser=None, cache=None):
        self.name = name
        self.requester = requester
        self.parser = parser
        self.cache = cache
        self.logger = get_logger(self.__class__.__name__.lower())

    def __await__(self):
        return self.update()

    async def update(self):
        response = await self.requester.request()
        data = self.parser.parse(response)
        if self.cache is not None:
            await self.cache.set(self.name, data)
        return data

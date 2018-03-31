"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
from crawler.requester import Requester
from crawler.parser import BaseParser
from crawler.grabber import Grabber
from crawler.cache import Cache


class Factory(object):
    def __init__(self, resources=None):
        self.resources = resources or []
        self.cache = None

    def load_meta(self):
        pass

    async def init_cache(self):
        self.cache = Cache()
        await self.cache._create_pool()

    def create(self):
        grabbers = []
        for res in self.resources:
            requester = Requester(base_url=res)
            parser = BaseParser()
            grabber = Grabber(
                base_url=res,
                requester=requester,
                parser=parser,
                cache=self.cache,
            )
            grabbers.append(grabber)
        return grabbers


def main():
    # Load description from yaml file
    resources = [
        'http://httpbin.org/get',
    ]
    factory = Factory(resources=resources)
    grabbers = factory.create()
    return grabbers[0]

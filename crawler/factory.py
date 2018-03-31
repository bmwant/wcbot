"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
from utils import get_logger
from crawler.requester import Requester
from crawler.parser import BaseParser
from crawler.grabber import Grabber
from crawler.cache import Cache


class Factory(object):
    def __init__(self, resources=None):
        name = self.__class__.__name__.lower()
        self.resources = resources or []
        self.cache = None
        self.logger = get_logger(name)

    def load_meta(self):
        self.logger.debug('Loading resources metainformation..')
        # Load description from yaml file
        resources = [
            'http://httpbin.org/get',
        ]
        self.resources = resources

    async def init_cache(self):
        self.logger.debug('Initializing cache...')
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

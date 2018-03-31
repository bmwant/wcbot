"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
import yaml

import config
from utils import get_logger
from crawler.models import Resource
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
        with open(config.RESOURCES_FILEPATH) as f:
            resources = yaml.load(f.read())
        self.resources = [Resource(**r) for r in resources]

    async def init_cache(self):
        self.logger.debug('Initializing cache...')
        self.cache = Cache()
        await self.cache._create_pool()

    def create(self):
        grabbers = []
        for res in self.resources:
            requester = Requester(base_url=res.url)
            parser = BaseParser()
            grabber = Grabber(
                name=res.name,
                requester=requester,
                parser=parser,
                cache=self.cache,
            )
            grabbers.append(grabber)
        return grabbers

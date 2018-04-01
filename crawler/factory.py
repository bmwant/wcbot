"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
import importlib

import yaml

import config
from utils import get_logger
from crawler.models import Resource
from crawler.requester import Requester
from crawler.grabber import Grabber
from crawler.cache import Cache


class Factory(object):
    def __init__(self, resources=None):
        self.resources = resources or []
        self.cache = None
        self.logger = get_logger(self.__class__.__name__.lower())

    def load_meta(self):
        self.logger.debug('Loading resources metainformation..')
        with open(config.RESOURCES_FILEPATH) as f:
            resources = yaml.load(f.read())
        self.resources = [Resource(**r) for r in resources]

    async def init_cache(self):
        self.logger.debug('Initializing cache...')
        self.cache = Cache()
        await self.cache._create_pool()

    def get_parser(self, parser_name):
        module_name = f'parser.{parser_name}'
        try:
            module = importlib.import_module(module_name, package=__package__)
        except ModuleNotFoundError:
            raise ValueError(
                f'No such parser: {parser_name}. Check resources meta file.')

        class_name = f'{parser_name}_parser'.title().replace('_', '')
        parser_cls = getattr(module, class_name, None)
        if parser_cls is None:
            raise ValueError(
                f'No such class {class_name} within module {module_name}.')
        return parser_cls()

    def create(self):
        grabbers = []
        for res in self.resources:
            requester = Requester(base_url=res.url)
            parser = self.get_parser(res.parser)
            grabber = Grabber(
                name=res.name,
                requester=requester,
                parser=parser,
                cache=self.cache,
            )
            grabbers.append(grabber)
        return grabbers

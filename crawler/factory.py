"""
Create `Grabber` instances for list of resources we need to grab information
from.
"""
import importlib

import yaml

import config
from utils import get_logger
from crawler.models import Resource
from crawler.grabber import Grabber
from crawler.cache import Cache


class Factory(object):
    def __init__(self, resources=None, teams=[]):
        self.resources = resources or []
        self.teams = teams or []
        self.cache = None
        self.logger = get_logger(self.__class__.__name__.lower())

    def load_resources(self):
        self.logger.debug('Loading resources..')
        with open(config.RESOURCES_FILEPATH) as f:
            resources = yaml.load(f.read())
        self.resources = [Resource(**r) for r in resources]

    def load_teams(self):
        self.logger.debug('Loading teams...')
        with open(config.TEAMS_FILEPATH) as f:
            teams = yaml.load(f.read())
        self.teams = teams

    async def init_cache(self):
        self.logger.debug('Initializing cache...')
        self.cache = Cache()
        await self.cache._create_pool()

    def get_parser(self, parser_name):
        module_name = f'{__package__}.parser.{parser_name}'
        try:
            module = importlib.import_module(module_name, package=__package__)
        except ModuleNotFoundError:
            raise ValueError(
                f'No such parser: {parser_name}. Check resources file syntax.')

        class_name = f'{parser_name}_parser'.title().replace('_', '')
        parser_cls = getattr(module, class_name, None)
        if parser_cls is None:
            raise ValueError(
                f'No such class {class_name} within module {module_name}.')
        return parser_cls()

    def get_fetcher(self, resource):
        fetcher_name = resource.fetcher
        module_name = f'{__package__}.fetcher.{fetcher_name}'
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            raise ValueError(
                f'No such fetcher: {fetcher_name}. '
                f'Check resources file syntax.'
            )

        class_name = f'{fetcher_name}_fetcher'.title().replace('_', '')
        fetcher_cls = getattr(module, class_name, None)
        if fetcher_cls is None:
            raise ValueError(
                f'No such class {class_name} within module {module_name}.')

        # todo: install proxy
        return fetcher_cls(base_url=resource.url)

    def create(self):
        grabbers = []
        for res in self.resources:
            fetcher = self.get_fetcher(res)
            parser = self.get_parser(res.parser)
            grabber = Grabber(
                name=res.name,
                fetcher=fetcher,
                parser=parser,
                cache=self.cache,
            )
            grabbers.append(grabber)
        return grabbers

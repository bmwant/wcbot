"""
Class handling requests to remote resources.
"""
from http import HTTPStatus

import aiohttp

from utils import get_logger
from crawler.fetcher import BaseFetcher


class SimpleFetcher(BaseFetcher):
    def __init__(self, base_url, *, proxy=None):
        super().__init__(base_url, proxy=proxy)
        self._session = None
        self.logger = get_logger(self.__class__.__name__.lower())

    @property
    def session(self):
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session is not None:
            await self._session.close()

    async def request(self, url=None):
        if url is None:
            url = self.base_url
        self.logger.info(f'Requesting {url}')
        async with self.session.get(url) as resp:
            if resp.status != HTTPStatus.OK:
                self.logger.debug(f'{url} respond {resp.status}')
            return await resp.text()

"""
Class handling requests to remote resources.
"""
import aiohttp


class Requester(object):
    def __init__(self, base_url, proxy=None):
        self.base_url = base_url
        self.proxy = proxy
        self._session = None

    def install_proxy(self, proxy):
        pass

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

        async with self.session.get(url) as resp:
            print(resp.status)
            return await resp.text()

"""
http://sports.williamhill.com
https://mobile.bet365.com
https://www.paddypower.com/bet
https://www.skybet.com
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

    async def request(self, url):
        async with self.session.get(url) as resp:
            print(resp.status)
            print(await resp.text())

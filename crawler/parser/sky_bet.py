from crawler.parser import BaseParser


class SkyBetParser(BaseParser):
    def parse(self, html):
        return html


async def process():
    from crawler.fetcher.browser import BrowserFetcher
    from crawler.proxy import Proxy
    event_url = 'https://m.skybet.com/football/world-cup-2018/event/16742642'
    base_url = 'https://www.skybet.com'
    proxy = Proxy(ip='163.172.175.210', port=3128)
    fetcher = SimpleFetcher(base_url=base_url, proxy=proxy)
    page = await fetcher.request(event_url)
    with open('f.html', 'w') as f:
        f.write(page)
    await fetcher.close()


def main():
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process())


if __name__ == '__main__':
    main()

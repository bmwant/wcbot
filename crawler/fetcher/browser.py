import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from utils import get_logger
from crawler.fetcher import BaseFetcher
from crawler.drivers.chrome import ChromeDriver


class BrowserFetcher(BaseFetcher):
    DEFAULT_DRIVER_WRAPPER = ChromeDriver
    DEFAULT_WAIT_TIME = 2

    def __init__(self, base_url, *,
                 driver_wrapper=None, xpath=None, proxy=None):
        super().__init__(base_url, proxy=proxy)
        if driver_wrapper is None:
            driver_wrapper = self.DEFAULT_DRIVER_WRAPPER()

        self.xpath = xpath
        self.driver = driver_wrapper.driver
        self.logger = get_logger(self.__class__.__name__.lower())

    async def request(self, url=None):
        if url is None:
            url = self.base_url

        self.logger.info(f'Requesting {url}')
        with ThreadPoolExecutor(max_workers=1) as executor:
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                executor, self._get, url, self.DEFAULT_WAIT_TIME)
        return await future

    def _get(self, url: str, wait: int=0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        # Wait for js on page to render
        time.sleep(wait)
        if self.xpath is not None:
            return self.driver. \
                find_element_by_xpath(self.xpath). \
                get_attribute('outerHTML')

        return self.driver.page_source

    def _close(self):
        self.driver.close()

    async def close(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(executor, self._close)
            await future


def main():
    from crawler.parser.paddy_power import PaddyPowerParser
    p = PaddyPowerParser()
    base_url = 'https://www.paddypower.com/bet'
    xpath = '/html/body/page-container/div/main/div/content-managed-page/div/div/div/div[3]/div/div[2]/div/avb-coupon/div/div'
    chrome_driver = ChromeDriver()
    f = BrowserFetcher(base_url, driver_wrapper=chrome_driver, xpath=xpath)
    resp = f._get(url=base_url, wait=3)
    p.parse(resp)


if __name__ == '__main__':
    main()

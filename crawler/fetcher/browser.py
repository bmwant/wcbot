import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from selenium.common.exceptions import NoSuchElementException

from utils import get_logger
from crawler.fetcher import BaseFetcher
from crawler.driver.chrome import ChromeDriver


class BrowserFetcher(BaseFetcher):
    DEFAULT_DRIVER_CLS = ChromeDriver
    DEFAULT_WAIT_TIME = 2

    def __init__(self, base_url, *,
                 driver_cls=None, xpath=None, proxy=None):
        super().__init__(base_url, proxy=proxy)

        driver_cls = driver_cls or self.DEFAULT_DRIVER_CLS
        proxy_uri = self._get_proxy_uri(proxy, driver_cls)
        driver_wrapper = driver_cls(proxy_uri=proxy_uri)

        self.driver = driver_wrapper.driver
        self.proxy_uri = proxy_uri
        self.xpath = xpath
        self.logger = get_logger(self.__class__.__name__.lower())

    def _get_proxy_uri(self, proxy, driver_cls):
        """
        Proxy format may vary based on browser driver used. This helpers allows
        to figure out which format is correct.
        """
        proxy_uri = None
        if proxy and driver_cls == ChromeDriver:
            proxy_uri = proxy.chrome_uri
        elif proxy:
            proxy_uri = proxy.uri

        return proxy_uri

    async def request(self, url=None):
        if url is None:
            url = self.base_url

        self.logger.info(f'Requesting {url} with proxy: {self.proxy_uri}')
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

        self._do_actions()
        return self.driver.page_source

    def _do_actions(self):
        """
        Make some actions on a page like clicking tabs or open collapsed elements.
        """
        try:
            # Add any logic for common elements here
            elem = self.driver.find_element_by_xpath(
                '//*[contains(text(), "Show More")]')
            elem.click()
        except NoSuchElementException:
            pass

    def _close(self):
        self.driver.close()

    async def close(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(executor, self._close)
            await future

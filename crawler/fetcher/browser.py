import time

from crawler.fetcher import BaseFetcher
from crawler.drivers.chrome import ChromeDriver


class BrowserFetcher(BaseFetcher):
    DEFAULT_DRIVER_WRAPPER = ChromeDriver

    def __init__(self, base_url, *,
                 driver_wrapper=None, xpath=None, proxy=None):
        super().__init__(base_url, proxy=proxy)
        if driver_wrapper is None:
            driver_wrapper = self.DEFAULT_DRIVER_WRAPPER()

        self.xpath = xpath
        self.driver = driver_wrapper.driver

    async def request(self, url=None):
        pass

    def _get(self, url: str, wait: int=0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        time.sleep(wait)
        if self.xpath is not None:
            return self.driver. \
                find_element_by_xpath(self.xpath). \
                get_attribute('outerHTML')

        return self.driver.page_source

    async def close(self):
        self.driver.close()


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

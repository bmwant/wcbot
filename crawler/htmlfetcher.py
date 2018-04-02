import time

from crawler.drivers.firefox import FirefoxDriver
from crawler.drivers.chrome import ChromeDriver


class HTMLFetcher(object):
    def __init__(self, driver_wrapper, xpath=None):
        self.xpath = xpath
        self.driver = driver_wrapper.driver

    def get(self, url: str, wait: int = 0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        time.sleep(wait)
        import pdb; pdb.set_trace()
        if self.xpath is not None:
            return self.driver.\
                find_element_by_xpath(self.xpath).\
                get_attribute('outerHTML')

        return self.driver.page_source

    def close(self) -> None:
        self.driver.close()


def main():
    from crawler.parser.paddy_power import PaddyPowerParser
    p = PaddyPowerParser()
    xpath = '/html/body/page-container/div/main/div/content-managed-page/div/div/div/div[3]/div/div[2]/div/avb-coupon/div/div'
    chrome_driver = ChromeDriver()
    f = HTMLFetcher(driver_wrapper=chrome_driver, xpath=xpath)
    url = 'https://www.paddypower.com/bet'
    resp = f.get(url, 3)
    p.parse(resp)


if __name__ == '__main__':
    main()

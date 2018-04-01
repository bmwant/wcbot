import time

from crawler.drivers.firefox import FirefoxDriver
from crawler.drivers.chrome import ChromeDriver


class HTMLFetcher(object):
    def __init__(self, driver):
        self.driver = driver

    def get(self, url: str, wait: int = 0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        time.sleep(wait)
        return self.driver.page_source

    def close(self) -> None:
        self.driver.close()


def main():
    firefox_driver = FirefoxDriver()
    chrome_driver = ChromeDriver()
    f = HTMLFetcher(driver=chrome_driver)
    url = 'https://www.paddypower.com/bet'
    resp = f.get(url)
    print(resp)


if __name__ == '__main__':
    main()

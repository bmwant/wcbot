import time

from crawler.drivers.firefox import FirefoxDriver
from crawler.drivers.chrome import ChromeDriver


class HTMLFetcher(object):
    def __init__(self, driver_wrapper):
        self.driver = driver_wrapper.driver

    def get(self, url: str, wait: int = 0) -> str:
        self.driver.delete_all_cookies()
        self.driver.get(url)
        import pdb; pdb.set_trace()
        time.sleep(wait)

        return self.driver.page_source

    def close(self) -> None:
        self.driver.close()


def main():
    # firefox_driver = FirefoxDriver()
    chrome_driver = ChromeDriver()
    f = HTMLFetcher(driver_wrapper=chrome_driver)
    url = 'https://www.paddypower.com/bet'
    resp = f.get(url, 3)
    with open('file.html', 'w') as f:
        f.write(resp)
    print(resp)


if __name__ == '__main__':
    main()

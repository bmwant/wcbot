import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import config


class Driver(object):
    pass


class FirefoxDriver(object):
    EXECUTABLE_PATH = config.GECKO_DRIVER_PATH

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument('-headless')

        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        firefox_profile.set_preference('permissions.default.image', 2)
        firefox_profile.set_preference(
            'dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        self._driver = webdriver.Firefox(
            executable_path=self.EXECUTABLE_PATH,
            firefox_options=firefox_options,
            log_path='/tmp/geckodriver.log',
            firefox_profile=firefox_profile,
        )
        self.driver.set_page_load_timeout(10)

    @property
    def driver(self):
        return self._driver


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
    f = HTMLFetcher(driver=firefox_driver)
    url = 'https://www.paddypower.com/bet'
    resp = f.get(url)
    print(resp)


if __name__ == '__main__':
    main()

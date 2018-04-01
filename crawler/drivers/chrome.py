from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from crawler.drivers import BaseDriver


class ChromeDriver(BaseDriver):
    BINARY_PATH = '/usr/bin/google-chrome'
    EXECUTABLE_PATH = config.CHROME_DRIVER_PATH

    def __init__(self):
        super().__init__()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.binary_location = self.BINARY_PATH

        driver = webdriver.Chrome(
            executable_path=self.EXECUTABLE_PATH,
            chrome_options=chrome_options,
        )
        self._driver = driver

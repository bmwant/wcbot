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
        chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

        driver = webdriver.Chrome(
            executable_path=self.EXECUTABLE_PATH,
            chrome_options=chrome_options,
        )
        self._driver = driver



"""
driver.get("http://www.duo.com")

magnifying_glass = driver.find_element_by_id("js-open-icon")
if magnifying_glass.is_displayed():
    magnifying_glass.click()
else:
    menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
menu_button.click()`

`search_field = driver.find_element_by_id("site-search")
search_field.clear()
search_field.send_keys("Olabode")
search_field.send_keys(Keys.RETURN)
assert "Looking Back at Android Security in 2016" in driver.page_source   driver.close()
"""

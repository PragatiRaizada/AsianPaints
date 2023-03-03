
from selenium import webdriver
from features.utility.ConfigClass import ConfigClass
from selenium.webdriver.chrome.options import Options

class UtilityClass:

    # All methods are created which are mandatory in the steps

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)
        self.driver.maximize_window()

    def launch_app(self):
        self.driver.get(ConfigClass.url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()

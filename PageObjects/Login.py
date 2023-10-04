from selenium.webdriver.common.by import By

from Utilities.readProperties import Reader
from TestCases.conftest import setup
from selenium import webdriver


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.facebook.com/login/"

    def clickLoginPage(self):
        print(self.base_url.title())

    def setFirstName(self, name1):
        name = self.driver.find_elements(By.XPATH, "//*[@id='email']")
        name.clear()
        name.sendkeys(name1)

    def setPassword(self, passwd):
        passwd = self.driver.find_elements(By.ID, "pass")
        passwd.clear()
        passwd.sendkeys(passwd)

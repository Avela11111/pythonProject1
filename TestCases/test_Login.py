from Utilities.readProperties import Reader
from TestCases.conftest import setup
from selenium import webdriver
from PageObjects.Login import Login


class test_Login:
    url1 = Reader.getLoginFacebook()
    user = Reader.getUsernameF()
    pin = Reader.getasswordF()

    def test_Start(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get(url1)

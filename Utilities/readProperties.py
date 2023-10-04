import configurations
import configparser

config = configparser.RawConfigParser()
config.read("\\configurations\\config.ini")


class Reader:

    @staticmethod
    def getLoginFacebook(self):
        url = config.get("Login", "URL")
        return url

    @staticmethod
    def getUsernameF():
        user = config.get("Login", "Username")
        return user

    @staticmethod
    def getasswordF():
        password = config.get("Login", "Password")

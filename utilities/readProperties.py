import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class readConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get('basic info', 'url')
        return url

    @staticmethod
    def getBrowser():
        browser = config.get('basic info', 'browser')
        return browser

    @staticmethod
    def getuserEmail():
        email = config.get('basic info', 'email')
        return email

    @staticmethod
    def getuserPassword():
        password = config.get('basic info', 'password')
        return password
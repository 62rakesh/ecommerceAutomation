import pytest
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_and_teardown")
class Test_01_Login:
    logs = LogGen.generateLog()

    def test_loginPageTitle(self):
        self.logs.info("login page title verification is started")
        act_title = self.driver.title
        if act_title == "Your store. Logins":
            print(act_title)
            self.logs.info("This test is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"loginPageTitle.png")
            self.logs.error("Title not found,this test is failed")
            assert False

    def test_userLogin(self):
        self.logs.info("userLogin verification started")
        lp = LoginPage(self.driver)
        self.logs.info("user entered a correct emailID")
        self.logs.info("user entered a correct password")
        self.logs.info("user clicked on the login button")
        lp.user_login(readConfig.getuserEmail(), readConfig.getuserPassword())
        self.logs.info("user is successfully logged in")




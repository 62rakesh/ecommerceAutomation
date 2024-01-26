import time
from selenium.webdriver.common.by import By


class LoginPage:
    user_email_id = "Email"
    user_password_id = "Password"
    login_btn_xpath = "(//BUTTON[contains(text(),'Log in')])"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, email):
        self.driver.find_element(By.ID, self.user_email_id).clear()
        self.driver.find_element(By.ID, self.user_email_id).send_keys(email)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.user_password_id).clear()
        self.driver.find_element(By.ID, self.user_password_id).send_keys(password)
        time.sleep(2)

    def click_loginBtn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        print("user is successfully logged in")
        time.sleep(5)

    def user_login(self, email, pwd):
        self.enter_username(email)
        self.enter_password(pwd)
        self.click_loginBtn()





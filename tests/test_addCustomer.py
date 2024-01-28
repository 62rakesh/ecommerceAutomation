import pytest

from pages.customerPage import customerPage
from pages.loginPage import LoginPage
from testdata.randomEmail import randomEmail
from utilities.customLogger import LogGen
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_and_teardown")
class Test_02_addCustomer:
    logs = LogGen.generateLog()
    random_email = randomEmail.randomEmailGenerator()

    def test_addCustomer(self):
        self.logs.info("userLogin verification started")
        lp = LoginPage(self.driver)
        self.logs.info("user entered a correct emailID")
        self.logs.info("user entered a correct password")
        self.logs.info("user clicked on the login button")
        lp.user_login(readConfig.getuserEmail(), readConfig.getuserPassword())
        self.logs.info("user is successfully logged in")
        self.logs.info("add customer verification is started")
        customer = customerPage(self.driver)
        customer.click_on_customer_link()
        self.logs.info("click on the customer link")
        customer.navigate_to_customer_page()
        self.logs.info("user navigates to the customer page")
        customer.click_add_New_customer_btn()
        self.logs.info("user clicked on the add new customer button")
        customer.enter_emailId(self.random_email)
        self.logs.info("user enters a correct emailID")
        customer.enter_firstName("TestFirstCustomer")
        self.logs.info("user enters a correct customer first name")
        customer.enter_lastName("TestLastCustomer")
        self.logs.info("user enters the lastname")
        customer.enter_password("Test1234#")
        self.logs.info("A correct password is entered")
        customer.select_gender("Male")
        self.logs.info("The customer gender is entered")
        customer.enter_dob("1/3/1995")
        self.logs.info("customer DOB is entered")
        customer.enter_companyName("TestCompany")
        self.logs.info("company name is entered")
        customer.check_tax_exempt()
        self.logs.info("checkbox is selected successfully")
        customer.select_customerRole("Registered")
        self.logs.info("customer role is selected")
        customer.save_customer()
        self.logs.info("A new customer is created successfully")

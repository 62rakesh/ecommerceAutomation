import pytest

from pages.customerPage import customerPage
from pages.customerRolePage import customerRole
from pages.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup_and_teardown")
class Test_04_addCustomerRole:
    logs = LogGen.generateLog()

    def test_addCustomerRole(self):
        self.logs.info("userLogin verification started")
        lp = LoginPage(self.driver)
        self.logs.info("user entered a correct emailID")
        self.logs.info("user entered a correct password")
        self.logs.info("user clicked on the login button")
        lp.user_login(readConfig.getuserEmail(), readConfig.getuserPassword())
        self.logs.info("user is successfully logged in")
        customer = customerPage(self.driver)
        self.logs.info("customer verification is started")
        customer.click_on_customer_link()
        self.logs.info("click on the customer link")
        role = customerRole(self.driver)
        self.logs.info("customer role verification is started")
        role.navigate_to_customer_role_page()
        self.logs.info("user navigate to the customer role page")
        role.click_add_customerRole_Btn()
        self.logs.info("user clicked on the add customer role button")
        role.enter_customerRole_Name("TestCustomer")
        self.logs.info("correct customer role is entered")
        role.check_FreeShipping_checkbox()
        self.logs.info("user clicked on the free shipping checkbox")
        role.check_taxExempt_checkbox()
        self.logs.info("user clicked on the taxExempt checkbox")
        role.select_Product("Apple MacBook Pro 13-inch")
        self.logs.info("user navigates to the search product page")
        self.logs.info("user selected a new product")
        role.enter_systemName("A new system for different customer role")
        self.logs.info("user enter a system name")
        role.save_customer_role()
        self.logs.info("A new customer role is created")


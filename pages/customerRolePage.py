import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class customerRole:
    customerRole_xpath = "(//P[contains(text(),' Customer roles')])"
    customerRole_title_xpath = "(//H1[@class='float-left'])"
    addNew_Btn_Role_xpath = "(//A[@class='btn btn-primary'])"
    customerRole_name_id = "Name"
    freeShipping_checkbox_id = "FreeShipping"
    taxExempt_id = "TaxExempt"
    choose_product_xpath = "(//BUTTON[@class='btn btn-primary'])[3]"
    System_Name_xpath = "(//INPUT[@class='form-control text-box single-line'])[2]"
    saveBtn_xpath = "(//BUTTON[@class='btn btn-primary'])[1]"
    product_name_1_xpath = "(//td[contains(text(),'Build your own computer')]/ancestor::tr[@class='odd']//*[contains(text(),'Select')])"
    product_name_2_xpath = "(//td[contains(text(),'Apple MacBook Pro 13-inch')]/ancestor::tr[@class='even']//*[contains(text(),'Select')])"
    search_product_id = "SearchProductName"
    search_btn_id = "search-products"
    systemName_id = "SystemName"

    def __init__(self, driver):
        # global driver
        # driver = webdriver.Chrome()
        self.driver = driver

    def navigate_to_customer_role_page(self):
        self.driver.find_element(By.XPATH, self.customerRole_xpath).click()
        time.sleep(2)
        title = self.driver.find_element(By.XPATH, self.customerRole_title_xpath).text
        if self.driver.find_element(By.XPATH, self.customerRole_title_xpath).is_displayed():
            print("user navigates to the customer role page")
            print("title of the page is:- " + title)
        else:
            print("test is failed")

    def click_add_customerRole_Btn(self):
        add_customerRole = self.driver.find_element(By.XPATH, self.addNew_Btn_Role_xpath)
        add_customerRole.click()
        time.sleep(2)
        print("user clicked on the add customer role button")

    def enter_customerRole_Name(self, name):
        roleName = self.driver.find_element(By.ID, self.customerRole_name_id)
        roleName.click()
        roleName.clear()
        roleName.send_keys(name)
        time.sleep(2)
        print(f"the customer is give a {name} role")

    def check_FreeShipping_checkbox(self):
        freeShipping_checkbox = self.driver.find_element(By.ID, self.freeShipping_checkbox_id)
        freeShipping_checkbox.click()
        print("For the above customer role the freeShipping checkbox is checked")

    def check_taxExempt_checkbox(self):
        taxExempt = self.driver.find_element(By.ID, self.taxExempt_id)
        taxExempt.click()
        print("for the above customer role the taxExempt is activated")
        time.sleep(1)

    def select_Product(self, productName):
        product = self.driver.find_element(By.XPATH, self.choose_product_xpath)
        product.click()
        self.driver.maximize_window()
        time.sleep(10)
        current_window = self.driver.current_window_handle
        print(current_window)
        print(self.driver.title)
        print("user navigates to a new window to select a product for the given customer role")
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            print("user switch to the child window now")
            print(self.driver.title)
            if self.driver.title.__eq__("Choose a product / nopCommerce administration"):
                time.sleep(5)
                if productName == "Build your own computer":
                    product = self.driver.find_element(By.XPATH, self.product_name_1_xpath)
                elif productName == "Apple MacBook Pro 13-inch":
                    product = self.driver.find_element(By.XPATH, self.product_name_2_xpath)
                else:
                    print("please enter a correct product")
                product.click()
                print("product name is:- " + productName)
                time.sleep(2)
                break
        self.driver.switch_to.window(current_window)
        time.sleep(5)
        print("A product is selected for the customer role")

    def enter_systemName(self, name):
        systemName = self.driver.find_element(By.ID, self.systemName_id)
        systemName.click()
        time.sleep(2)
        systemName.send_keys(name)
        print(f"name of the system is:- "+name)

    def save_customer_role(self):
        save = self.driver.find_element(By.XPATH, self.saveBtn_xpath)
        save.click()
        time.sleep(4)




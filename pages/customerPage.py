import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class customerPage:
    customer_page_xpath = "(//LI[@class='nav-item has-treeview'])[4]"
    customer_link_xpath = "(//ul//li//a//p[contains(text(),' Customers')])[1]"
    customer_title_xpath = "(//H1[@class='float-left'])"
    addNew_Btn_xpath = "(//A[@class='btn btn-primary'])"
    email_id = "Email"
    password_id = "Password"
    first_Name_id = "FirstName"
    last_name_id = "LastName"
    gender_id = "Gender_Male"
    dob_id = "DateOfBirth"
    company_name_id = "Company"
    vendor_name_id = "VendorId"
    is_tax_exempt_id = "IsTaxExempt"
    customer_roles_xpath = "(//DIV[@class='k-multiselect-wrap k-floatwrap'])[2]"
    select_customer_role_registered_xpath = "(//LI[contains(text(),'Registered')])"
    select_customer_role_adminstrator_xpath = "(//LI[contains(text(),'Administrators')])"
    select_customer_role_vendor_xpath = "(//LI[contains(text(),'Vendors')])"
    select_customer_role_guest_xpath = "(//LI[contains(text(),'Guests')])"
    delete_selected_role_xpath = "(//SPAN[@class='k-select'])[2]"
    save_btn_xpath = "(//BUTTON[@class='btn btn-primary'])[1]"
    warning_message_xpath = "(//DIV[@class='validation-summary-errors'])"
    success_message_xpath = "(//DIV[@class='alert alert-success alert-dismissable'])"

    def __init__(self, driver):
        self.driver = driver
        # global driver
        # driver = webdriver.Chrome()

    def click_on_customer_link(self):
        self.driver.find_element(By.XPATH, self.customer_page_xpath).click()
        time.sleep(2)

    def navigate_to_customer_page(self):
        self.driver.find_element(By.XPATH, self.customer_link_xpath).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, self.customer_title_xpath).is_displayed():
            title = self.driver.find_element(By.XPATH, self.customer_title_xpath).text
            print(title)
            assert True

        else:
            self.driver.save_screenshot(".\\screenshot\\customer.png")
            assert False

    def click_add_New_customer_btn(self):
        self.driver.find_element(By.XPATH, self.addNew_Btn_xpath).click()
        time.sleep(3)

    def enter_emailId(self, email):
        self.driver.find_element(By.ID, self.email_id).click()
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        print("email id is:- "+email)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).click()
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        print("user enters a password")
        time.sleep(1)

    def enter_firstName(self,FNAME):
        self.driver.find_element(By.ID, self.first_Name_id).click()
        self.driver.find_element(By.ID, self.first_Name_id).clear()
        self.driver.find_element(By.ID, self.first_Name_id).send_keys(FNAME)
        print("first name is:- " +FNAME)
        time.sleep(1)

    def enter_lastName(self, Lname):
        self.driver.find_element(By.ID, self.last_name_id).click()
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(Lname)
        print("first name is:- " + Lname)
        time.sleep(1)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.gender_id).click()
            time.sleep(1)
        elif gender == "Female":
            self.driver.find_element(By.ID, self.gender_id).click()
            time.sleep(1)
        else:
            print("Please select a gender")

    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.dob_id).click()
        self.driver.find_element(By.ID, self.dob_id).send_keys(dob)
        time.sleep(2)

    def enter_companyName(self, comapnyName):
        self.driver.find_element(By.ID, self.company_name_id).click()
        self.driver.find_element(By.ID, self.company_name_id).clear()
        self.driver.find_element(By.ID, self.company_name_id).send_keys(comapnyName)
        print("companyName is:- "+comapnyName)
        time.sleep(2)

    def check_tax_exempt(self):
        self.driver.find_element(By.ID, self.is_tax_exempt_id).click()
        time.sleep(3)

    def select_customerRole(self, role):
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(By.XPATH, self.delete_selected_role_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.customer_roles_xpath).click()
        time.sleep(2)
        if role == "Registered":
            Role = self.driver.find_element(By.XPATH, self.select_customer_role_registered_xpath)
        elif role == "Administrators":
            Role = self.driver.find_element(By.XPATH, self.select_customer_role_adminstrator_xpath)
        elif role == "Vendors":
            Role = self.driver.find_element(By.XPATH, self.select_customer_role_vendor_xpath)
        else:
            Role = self.driver.find_element(By.XPATH, self.select_customer_role_guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click()", Role)
        print("Role is:- "+role)

    def save_customer(self):
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()
        print("customer is saved successfully")
        time.sleep(5)
        if self.driver.find_element(By.XPATH, self.success_message_xpath).is_displayed():
            success = self.driver.find_element(By.XPATH, self.success_message_xpath).text
            print("customer is created:- "+success)
        elif self.driver.find_element(By.XPATH, self.warning_message_xpath).is_displayed():
            warning = self.driver.find_element(By.XPATH, self.warning_message_xpath).text
            print("warning message is:- "+warning)
        else:
            print("The customer creation is failed")
            self.driver.save_screenshot(".\\screenshot\\saveCustomer.png")










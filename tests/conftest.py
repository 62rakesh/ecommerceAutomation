import pytest
from selenium import webdriver

from utilities.readProperties import readConfig


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = readConfig.getBrowser()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("Edge"):
        driver = webdriver.Edge()
    else:
        print("Please select a browser from the given list chrome/firefox/edge")
    driver.maximize_window()
    driver.get(readConfig.getApplicationUrl())
    request.cls.driver = driver
    yield
    driver.quit()

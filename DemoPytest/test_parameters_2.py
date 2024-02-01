from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    yield
    print("Close Driver")
    driver.close()


@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass


class Test_Drivers(BaseClass):
    def test_multiple_browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.CSS_SELECTOR,"div#__next h1").text
        print("Header: ", header)
        assert header == "Selenium Playground"

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
  print("Start Test With Automatic Fixture")

@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email") \
        .send_keys("pytestpython@gmail.com")
    driver.find_element(By.ID, "input-password") \
        .send_keys("abcd@1234")
    driver.find_element(By.XPATH,
                        "//input[@value='Login']").click()
    print("Log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Logout").click()
    print("Log Out")


def test1_order_history_title(setup_teardown):
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Order").click()
    assert driver.title == "Order History"
    print("Test 1 Is Complete")


def test2_change_password_title(setup_teardown):
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Password").click()
    assert driver.title == "Change Password"
    print("Test 2 Is Complete")

# def test1():
#     print("Login In")
#     print("Execute Test 1")
#     print("Login Out")
#
#
# def test2():
#     print("Login In")
#     print("Execute Test 2")
#     print("Login Out")

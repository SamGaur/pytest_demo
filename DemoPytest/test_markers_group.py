from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.integration
@pytest.mark.smoke
def test_ajax_form_submit():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

    driver.find_element(By.XPATH, "//input[@id='title']").send_keys("Samiksha")
    driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Samiksha is learning PyTest Framework.")
    driver.find_element(By.XPATH, "//input[@id='btn-submit']").click()
    request = driver.find_element(By.ID, "submit-control").text
    assert request.__contains__("Processing")


def test_e2e():
    print("End to End Test")

@pytest.mark.smoke
def test_login():
    print("Login to application.")

@pytest.mark.smoke
def test_logout():
    print("Logout")


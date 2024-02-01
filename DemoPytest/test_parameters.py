import math

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("num1,num2,expected_total",
                         [
                             ("25", "25", "50"),
                             ("10", "10", "30"),
                             ("30", "10", "40")
                         ])
def test_sum(num1, num2, expected_total):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.XPATH, "//input[@id='sum1']").send_keys(num1)
    driver.find_element(By.XPATH, "//input[@id='sum2']").send_keys(num2)
    driver.find_element(By.XPATH, "//button[text()='Get Sum']").click()

    actual_total = driver.find_element(By.ID, "addmessage").text
    assert actual_total == expected_total, \
        "Actual & Expected Total do not match."


@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_raising_base_to_power(base, exponent):
    result = base ** exponent
    assert result == math.pow(base, exponent)

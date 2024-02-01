from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def test_find_iphone():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH, "//div[@id='entry_217822']//input[@placeholder='Search For Products']").send_keys(
        "iphone")
    driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

    search_value = driver.find_element(By.XPATH, "//h1[contains(text(),'Search')]").text
    assert "Search - iphone" in search_value

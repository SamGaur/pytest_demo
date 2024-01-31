from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_text_by_sending():
    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    title_name = driver.find_element(By.XPATH, "//h1[normalize-space()='Simple Form Demo']").text
    assert "Simple Form Demo" in title_name

    driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("PyTest")
    driver.find_element(By.XPATH, "//button[@id='showInput']").click()

    driver.find_element(By.ID, "showInput").click()
    message = driver.find_element(By.ID, "message").text
    assert message == "PyTest"

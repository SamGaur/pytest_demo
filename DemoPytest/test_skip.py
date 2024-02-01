from datetime import datetime

from selenium import webdriver
import pytest


class TestLambdaTest:
    def test_sample_app_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://lambdatest.github.io/sample-todo-app/")
        pytest.skip()  # Skip test during execution
        expected_title = "Sample page - lambdatest.com"
        assert expected_title == driver.title

## Using Skip Decorator
##Purpose is to collect the item but not execute/run; item will get skip at the execution stage.
    @pytest.mark.skip(reason = "Code has not been deployed in Prod Environment.")
    def test_ecommerce_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17")
        expected_title = "Software"
        assert expected_title == driver.title

    @pytest.mark.skip()
    def test_special_offers(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/special")
        expected_title = "Special Offers"
        assert expected_title == driver.title

    @pytest.mark.skipif(
        datetime.now() >= datetime(2080, 7, 18),
        reason= "Repo is Not Complete ")
    def test_github(self):
        driver = webdriver.Chrome()
        driver.get("https://github.com/SamGaur")
        expected_title = "SamGaur"
        print("Title: ", expected_title)
        assert expected_title
        driver.title.__contains__(expected_title)

        
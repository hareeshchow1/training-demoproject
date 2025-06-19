import sys
import os
import pytest
from selenium import webdriver

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from config.creds import USERNAME, PASSWORD, FACEBOOK_URL
import time

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_facebook_login(driver):
    driver.get(FACEBOOK_URL)
    login_page = LoginPage(driver)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login()
    time.sleep(3)
    # Add assertions for successful login

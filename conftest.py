import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.auth_page import LoginPage
from urls import base_url


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.page_load_strategy = "eager"
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-cache")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)

    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver, base_url)
    return page

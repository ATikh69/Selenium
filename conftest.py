import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = "C:/Users/Aleksey.Tikhonov/Downloads/drivers/chromedriver"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", action="store", default='https://192.168.1.88:8081')
    parser.addoption("--driver_folder", default="C:/Users/Aleksey.Tikhonov/Downloads/drivers/chromedriver")


@pytest.fixture()
def browser(request):
    driver = None
    url = request.config.getoption("--url")
    browser_name = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(os.path.join(driver_folder,'chromedriver.exe')))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(os.path.join(driver_folder,'geckodriver.exe')))

    yield driver

    driver.quit()

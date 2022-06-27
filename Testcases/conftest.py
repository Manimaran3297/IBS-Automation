import os
from datetime import datetime

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'Chrome':
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="Chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('Reports'):
        os.makedirs('Reports')
    config.option.htmlpath = 'reports/report_' + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"




















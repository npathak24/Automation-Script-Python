from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#### pytest html reports ####
def pytest_configure(config):
    config.metadata['Project Name'] = 'salesforce automation test'
    config.metadata['Module Name'] = 'login'
    config.metadata['Tester'] = 'naman'

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
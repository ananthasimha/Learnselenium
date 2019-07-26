import pytest
from selenium import webdriver

@pytest.fixture()
def OnetimeSetup(request,browser):
    print("RUnning the Onetime SetUp")
    if browser=="firefox":
        value=webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
    else:
        value=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    if request.cls is not None:
        request.cls.value=value



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


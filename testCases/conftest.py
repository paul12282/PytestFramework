from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    return webdriver.Chrome(executable_path="C:\Drivers\Chromedriver_32\chromedriver.exe")

def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation learning'
    config._metadata['Module Name'] = 'Websites'
    config._metadata["Tester name"] = 'Paul'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


#Command: -s -v --html=Reports\report.html


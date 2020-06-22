#Contents of conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
	print("initiating chrome driver")
	driver = webdriver.Chrome('C:\Program Files\webdrivers\chromedriver.exe')
	yield driver
	driver.quit()
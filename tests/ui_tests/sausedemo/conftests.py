import pytest
from selenium.webdriver import Chrome
from qa_python_cource_hillel.core.ui.sausedemo.pages.login_page import LoginPage
from qa_python_cource_hillel.core.ui.sausedemo.pages.products_page import ProductsPage


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def products_page(driver):
    return ProductsPage(driver)
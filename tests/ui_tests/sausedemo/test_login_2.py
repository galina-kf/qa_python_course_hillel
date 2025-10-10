import pytest
from selenium.webdriver import Chrome
from qa_python_cource_hillel.core.ui.sausedemo.pages.login_page import LoginPage
from qa_python_cource_hillel.core.ui.sausedemo.pages.products_page import ProductsPage

@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

def test_product_page_is_open(driver):

    login_page = LoginPage(driver)
    login_page.open_page()

    login_page.login_user('standard_user', 'secret_sauce')

    products_page = ProductsPage(driver)
    products_page.products_images()


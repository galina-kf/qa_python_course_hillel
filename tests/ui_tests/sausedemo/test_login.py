import pytest
import pytest_check
import allure

@allure.feature("Login functionality")
@allure.story("Login with valid credentials")
def test_product_page_is_open(driver, login_page, products_page):
   login_page.login_user('standard_user', 'secret_sauce')
   products_page.products_images()

@allure.feature("Login functionality")
@allure.story("Login with invalid credentials")
@pytest.mark.parametrize("user_name,password", [
   ("placeholder", "secret_sauce"),
   ("standard_user", "placeholder")])
def test_incorrect_credentials(user_name, password, driver, login_page):
   login_page.login_user(user_name, password)
   # login_page.error_crosses()
   # login_page.error_h3_text()
   pytest_check.equal(login_page.get_error_crosses_number(), 3)
   pytest_check.equal(login_page.get_error_message(), "Epic sadface: Username and password do not match any user in this service")


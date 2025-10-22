import pytest
import pytest_check
import allure

@allure.feature("Login functionality")
@allure.story("Login with valid credentials")
def test_product_page_is_open(driver, login_page, products_page):
   with allure.step("Open login page, enter valid credentials"):
      login_page.login_user('standard_user', 'secret_sauce')
   with allure.step("Verify that products page opens"):
      products_page.products_images()

@allure.feature("Login functionality")
@allure.story("Login with invalid credentials")
@pytest.mark.parametrize("user_name,password", [
   ("placeholder", "secret_sauce"),
   ("standard_user", "placeholder")])
def test_incorrect_credentials(user_name, password, driver, login_page):
   with allure.step("Open login page, enter invalid credentials"):
      login_page.login_user(user_name, password)
   with allure.step("Check that error crosses"):
      pytest_check.equal(login_page.get_error_crosses_number(), 3)
   with allure.step("Check error message"):
      pytest_check.equal(login_page.get_error_message(), "Epic sadface: Username and password do not match any user in this service")


#from settings import settings
import pytest_check
import allure

@allure.feature("Products page functionality")
@allure.story("Check the default sorting of products")
def test_default_sorting(driver, login_page, products_page):
    with allure.step("Open login page, enter invalid credentials"):
        login_page.login_user('standard_user', 'secret_sauce')
    with allure.step("Check default soring option"):
        pytest_check.equal(products_page.get_current_select_option(), products_page.default_sort_option)
    with allure.step("Check actual soring option and compare with existing"):
        actual_sorting = products_page.get_product_name_as_text()
        expected_sorting = sorted(actual_sorting)
        pytest_check.equal(actual_sorting, expected_sorting)
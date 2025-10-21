import pytest
from selenium.webdriver import Chrome
from core.ui.qauto2forstudy.pages.registration_page import RegistrationPage
from core.ui.qauto2forstudy.pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

@pytest.fixture
def registration_page(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_page()
    return RegistrationPage(driver)

@pytest.fixture
def check_new_url(driver):
    assert(driver.current_url == "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"),\
            "Incorrect URL opens after registration"

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page



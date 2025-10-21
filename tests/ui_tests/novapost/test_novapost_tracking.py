import pytest
import allure
from selenium.webdriver import Chrome
from qa_python_cource_hillel.core.ui.novapost.pages.tracking_page import TrackingPage

@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

@allure.feature("Nova Post Functionality")
@allure.story("Nova Post Parcel Tracking")
def test_tracking_number(driver):
    with allure.step("Open Nova Posta page"):
        np_page = TrackingPage(driver)
        np_page.open_page()

    with allure.step("Enter valid tracking number to search"):
        tr_number = 59001469231545
        np_page.start_search(tr_number=tr_number)
    with allure.step("Check the parcel status"):
        # step to close info when user comes to the page at first time
        np_page.check_first_visit_info()
        np_page.get_status()








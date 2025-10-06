import pytest
from selenium.webdriver import Chrome
from qa_python_cource_hillel.core.ui.novapost.pages.tracking_page import TrackingPage

@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()


def test_tracking_number(driver):

    np_page = TrackingPage(driver)
    np_page.open_page()

    tr_number = 59001469231545
    np_page.start_search(tr_number=tr_number)

    # step to close info when user comes to the page at first time
    np_page.check_first_visit_info()

    np_page.get_status()








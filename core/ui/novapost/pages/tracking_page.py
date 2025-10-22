from core.ui.novapost.locators.tracking_page_locators import TrackingPageLocators
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException


class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://tracking.novaposhta.ua/#/uk/"
        self.locators = TrackingPageLocators

    def _tracking_input(self):
        return self._get_element(self.locators.input_field)

    def _submit_btn(self):
        return self._get_element(self.locators.submit_btn)

    def _status_text(self):
        return self._get_status(self.locators.parsel_status)

    def first_visit_info(self):
        return self._get_element(self.locators.first_visit_info_btn)

    def tracking_enter(self, tr_number):
        self._tracking_input().send_keys(tr_number)
        return self

    def start_search(self, tr_number):
        self.tracking_enter(tr_number)
        self._submit_btn().click()

    def check_first_visit_info(self):
        try:
            self.first_visit_info()
            self.first_visit_info().click()
        except TimeoutException as e:
            print(f'"First visit info is absent {e}"')

    def get_status(self):
        if self._status_text():
            print(f'The current parsel status: {self._status_text().text}')

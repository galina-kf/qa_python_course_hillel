from core.ui.qauto2forstudy.pages.base_page import BasePage
from core.ui.qauto2forstudy.locators.main_page_locators import MainPageLocators
from settings import settings

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        #self.url = settings.MAIN_URL
        self.url = "https://qauto2.forstudy.space/panel/garage"
        self.locators = MainPageLocators

    def check_header_items(self):
        self._page_elem(self.locators.header)
        self._page_elems(self.locators.header_garage)
        self._page_elems(self.locators.header_fuel_exp)
        self._page_elems(self.locators.header_instructions)


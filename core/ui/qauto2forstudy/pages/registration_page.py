from core.ui.qauto2forstudy.pages.base_page import BasePage
from core.ui.qauto2forstudy.locators.registration_page_locators import RegistrationPageLocators
from core.ui.qauto2forstudy.locators.home_page_locators import HomePageLocators
from settings import settings

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        #self.url = settings.BASE_URL
        # self.name = settings.name
        # self.last_name = settings.last_name
        # self.email = settings.email
        # self.password = settings.password

        self.url = "https://guest:welcome2qauto@qauto2.forstudy.space"
        self.name = "AAA"
        self.last_name = "BBB"
        self.email = "try123@gmail.com"
        self.password = "HillelCourse25"
        self.home_locators = HomePageLocators
        self.locators = RegistrationPageLocators

    def submit_signin_btn(self):
        self.click_button(self._button(HomePageLocators.sign_up_btn))
        return self

    def dialog_window(self):
        self._page_elem(RegistrationPageLocators.dialog_window)
        return self

    def get_dialog_window(self):
        self.submit_signin_btn()
        self.dialog_window()
        return self

    def fill_forms(self):
        self.enter_value(RegistrationPageLocators.name_field, self.name)
        self.enter_value(RegistrationPageLocators.last_name_field, self.last_name)
        self.enter_value(RegistrationPageLocators.email_field, self.email)
        self.enter_value(RegistrationPageLocators.password_field, self.password)
        self.enter_value(RegistrationPageLocators.password_again, self.password)
        self.click_button(RegistrationPageLocators.btn_register)

    def get_name_field(self):
        self._page_elem(RegistrationPageLocators.name_field)

    def get_last_name(self):
        self._page_elem(RegistrationPageLocators.last_name_field)

    def get_email(self):
        self._page_elem(RegistrationPageLocators.email_field)


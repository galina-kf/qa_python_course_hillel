from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self.driver.get(url)

    def _get_element(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((locator)))

    def _button(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((locator)))

    def _get_status(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located(locator))

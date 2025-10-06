from selenium.webdriver.common.by import By


class TrackingPageLocators:
    input_field = (By.XPATH, "//input[@class='track__form-group-input']")
    submit_btn = (By.XPATH, "//input[@id='np-number-input-desktop-btn-search-en']")
    parsel_status = (By.XPATH, "//div[@class='header__status-text']")
    first_visit_info_btn = (By.XPATH, "//div[@class='first-visit-helper-wrapper d-flex flex-column tracking-desktop']/button")


from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    dialog_window = (By.XPATH, "//div[@class='modal-content']")
    dialog_header = (By.XPATH, "//div[@class='modal-header']")
    signup_form = (By.XPATH, "//div[@class='modal-body']")
    name_field = (By.XPATH, "//input[@id='signupName']")
    last_name_field = (By.XPATH, "//input[@id='signupLastName']")
    email_field = (By.XPATH, "//input[@id='signupEmail']")
    password_field = (By.XPATH, "//input[@id='signupPassword']")
    password_again = (By.XPATH, "//input[@id='signupRepeatPassword']")
    btn_register = (By.XPATH, "//button[@class='btn btn-primary']")

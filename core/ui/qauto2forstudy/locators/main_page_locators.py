from selenium.webdriver.common.by import By

class MainPageLocators:
    header = (By.XPATH, "//a[@class='header_logo']")
    header_garage = (By.XPATH, "//a[@routerlink='/panel/garage'][1]")
    header_fuel_exp = (By.XPATH, "//a[@routerlink='/panel/expenses'][1]")
    header_instructions = (By.XPATH, "//a[@routerlink='/panel/instructions'][1]")
    my_profile_btn = (By.XPATH, "//button[@id='userNavDropdown']")

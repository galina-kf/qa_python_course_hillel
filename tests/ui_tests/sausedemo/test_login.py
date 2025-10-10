from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_is_open():
    driver = Chrome()
    driver.get('https://www.saucedemo.com')

    user_name = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys('standard_user')

    password = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys('secret_sauce')

    login_btn = WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, "login-button")))
    login_btn.click()

    WebDriverWait(driver, timeout=5).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                "//div[@class='inventory_item_img']")))

    driver.quit()

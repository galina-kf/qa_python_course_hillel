import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()

webdriver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
time.sleep(5)

header_button_home = webdriver.find_element(By.XPATH, value="//nav/a").text

header_button_about = webdriver.find_element(By.XPATH, value="//nav/button[1]").text

header_button_contacts = webdriver.find_element(By.XPATH, value="//nav/button[2]").text

head_button_guest_login = webdriver.find_element(By.XPATH, value="//div/div/div[2]/button[1]").text

head_button_sign_in = webdriver.find_element(By.XPATH, value="//div/div/div[2]/button[2]").text

body_button_sign_up = webdriver.find_element(By.XPATH, value="//div/div[@class='hero-descriptor']/button").text

youtube_frame = webdriver.find_element(By.XPATH, value="//div/div/iframe")
print(youtube_frame.get_attribute('src'))

# switch to the extra layer youtube iframe
webdriver.switch_to.frame(youtube_frame)

hillel_logo = webdriver.find_element(By.XPATH, value="//a[@class='ytp-title-channel-logo']")
print(hillel_logo.get_attribute('href'))

search_btn = webdriver.find_element(By.XPATH, value="//div[@class='ytp-chrome-top-buttons']/button[1]")
print(search_btn.get_attribute('aria-label'))

watch_later_btn = webdriver.find_element(By.XPATH, value="//div[@class='ytp-chrome-top-buttons']/button[2]")
print(watch_later_btn.get_attribute('aria-label'))

share_btn = webdriver.find_element(By.XPATH, value="//div[@class='ytp-chrome-top-buttons']/button[3]")
print(share_btn.get_attribute('aria-label'))

youtube_play_btn = webdriver.find_element(By.XPATH, value="//button[@title='Play']")
print(youtube_play_btn.get_attribute('aria-label'))

# return to the base page layer
webdriver.switch_to.default_content()



#webdriver.find_element(By.XPATH, value="//*[@id='main']/food")


webdriver.quit()





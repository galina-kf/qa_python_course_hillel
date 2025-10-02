import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()

webdriver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
time.sleep(5)

# header elements

header_button_home = webdriver.find_element(By.CSS_SELECTOR, value="a[class='btn header-link -active']")
print(header_button_home.text)

header_button_about = webdriver.find_elements(By.CSS_SELECTOR, value="button[class='btn header-link']")[0]
print(header_button_about.text)

header_button_contacts = webdriver.find_elements(By.CSS_SELECTOR, value="button[class='btn header-link']")[1]
print(header_button_contacts.text)

header_btn_guest_login = webdriver.find_element(By.CSS_SELECTOR, value="button[class='header-link -guest']")
print(header_btn_guest_login.text)

header_btn_sign_in = webdriver.find_element(By.CSS_SELECTOR, value="button[class='btn btn-outline-white header_signin']")
print(header_btn_sign_in.text)

# Guest part elements

body_button_sign_up = webdriver.find_element(By.CSS_SELECTOR, value="button[class='hero-descriptor_btn btn btn-primary']")
print(body_button_sign_up.text)

ytb_frame = webdriver.find_element(By.CSS_SELECTOR, value="iframe[class='hero-video_frame']")
print(ytb_frame.get_attribute('src'))

# switch to the layer youtube iframe
webdriver.switch_to.frame(ytb_frame)

hillel_logo = webdriver.find_element(By.CSS_SELECTOR, value="a[class='ytp-title-channel-logo']")
print(hillel_logo.get_attribute('href'))

search_btn = webdriver.find_element(By.CSS_SELECTOR, value="button[class='ytp-button ytp-search-button ytp-show-search-title']")
print(search_btn.get_attribute('aria-label'))

watch_later_btn = webdriver.find_element(By.CSS_SELECTOR, value="button[class='ytp-watch-later-button ytp-button ytp-show-watch-later-title']")
print(watch_later_btn.get_attribute('aria-label'))

share_btn = webdriver.find_element(By.CSS_SELECTOR, value="button[class='ytp-button ytp-share-button ytp-show-share-title ytp-share-button-visible']")
print(share_btn.get_attribute('aria-label'))

youtube_play_btn = webdriver.find_element(By.CSS_SELECTOR, value="button[class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
print(youtube_play_btn.get_attribute('aria-label'))

# return to the base page layer
webdriver.switch_to.default_content()

# About section elements

about_section_img_1 = webdriver.find_elements(By.CSS_SELECTOR, value="img[class='about-picture_img']")[0]
print(about_section_img_1.get_attribute('src'))

about_section_title_1 = webdriver.find_elements(By.CSS_SELECTOR, value="p[class='about-block_title h2']")[0]
print(about_section_title_1.text)

about_section_text_1 = webdriver.find_elements(By.CSS_SELECTOR, value="p[class='about-block_descr lead']")[0]
print(about_section_text_1.text)

about_section_img_2 = webdriver.find_elements(By.CSS_SELECTOR, value="img[class='about-picture_img']")[1]
print(about_section_img_2.get_attribute('src'))

about_section_title_2 = webdriver.find_elements(By.CSS_SELECTOR, value="p[class='about-block_title h2']")[1]
print(about_section_title_2.text)

about_section_text_2 = webdriver.find_elements(By.CSS_SELECTOR, value="p[class='about-block_descr lead']")[1]
print(about_section_text_2.text)

# Contacts section elements

# no understanding how to get text Contact
contacts_header = webdriver.find_element(By.CSS_SELECTOR, value="#contactsSection h2")
print(contacts_header.text)

fb_icon = webdriver.find_elements(By.CSS_SELECTOR, value="a[class='socials_link']")[0]
print(fb_icon.get_attribute('href'))

telegram_icon = webdriver.find_elements(By.CSS_SELECTOR, value="a[class='socials_link']")[1]
print(telegram_icon.get_attribute('href'))

ytb_icon = webdriver.find_elements(By.CSS_SELECTOR, value="a[class='socials_link']")[2]
print(ytb_icon.get_attribute('href'))

instagram_icon = webdriver.find_elements(By.CSS_SELECTOR, value="a[class='socials_link']")[3]
print(instagram_icon.get_attribute('href'))

linkedin_icon = webdriver.find_elements(By.CSS_SELECTOR, value="a[class='socials_link']")[4]
print(linkedin_icon.get_attribute('href'))

hillel_link = webdriver.find_element(By.CSS_SELECTOR, value="a[class='contacts_link display-4']")
print(hillel_link.get_attribute('href'))

hillel_email = webdriver.find_element(By.CSS_SELECTOR, value="a[class='contacts_link h4']")
print(hillel_email.get_attribute('href'))

webdriver.quit()


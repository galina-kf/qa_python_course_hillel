import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()

webdriver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
time.sleep(5)
# header elements
header_button_home = webdriver.find_element(By.XPATH, value="//nav/a")
print(header_button_home.text)

header_button_about = webdriver.find_element(By.XPATH, value="//nav/button[1]")
print(header_button_about.text)

header_button_contacts = webdriver.find_element(By.XPATH, value="//nav/button[2]")
print(header_button_contacts.text)

header_button_guest_login = webdriver.find_element(By.XPATH, value="//div/div/div[2]/button[1]")
print(header_button_guest_login.text)

header_button_sign_in = webdriver.find_element(By.XPATH, value="//div/div/div[2]/button[2]")
print(header_button_sign_in.text)

# guest part element
body_button_sign_up = webdriver.find_element(By.XPATH, value="//div/div[@class='hero-descriptor']/button")
print(body_button_sign_up.text)

youtube_frame = webdriver.find_element(By.XPATH, value="//div/div/iframe")
print(youtube_frame.get_attribute('src'))

# switch to the layer youtube iframe
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

# About section elements

about_section_img_1 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[1]/div/div/img")
print(about_section_img_1.get_attribute('src'))

about_section_title_1 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[1]/div/p").text
print(about_section_title_1)

about_section_text_1 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[1]/div/p[2]").text
print(about_section_text_1)

about_section_img2 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[2]/div/div/img")
print(about_section_img2.get_attribute('src'))

about_section_title_2 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[2]/div/p").text
print(about_section_title_2)

about_section_text_2 = webdriver.find_element(By.XPATH, value="//div[@class='section about']/div/div/div[2]/div/p[2]").text
print(about_section_text_2)

# Contacts section elements
contacts_header = webdriver.find_element(By.XPATH, value="//div[@id='contactsSection']/div/div/div/h2").text
print(contacts_header)

fb_icon = webdriver.find_element(By.XPATH, value="//div[@class='contacts_socials socials']/a")
print(fb_icon.get_attribute('href'))

telegram_icon = webdriver.find_element(By.XPATH, value="//div[@class='contacts_socials socials']/a[2]")
print(telegram_icon.get_attribute('href'))

ytb_icon = webdriver.find_element(By.XPATH, value="//div[@class='contacts_socials socials']/a[3]")
print(ytb_icon.get_attribute('href'))

instagram_icon = webdriver.find_element(By.XPATH, value="//div[@class='contacts_socials socials']/a[4]")
print(instagram_icon.get_attribute('href'))

linkedin_icon = webdriver.find_element(By.XPATH, value="//div[@class='contacts_socials socials']/a[5]")
print(linkedin_icon.get_attribute('href'))

hillel_link = webdriver.find_element(By.XPATH, value="//a[@class='contacts_link display-4']")
print(hillel_link.get_attribute('href'))

hillel_email = webdriver.find_element(By.XPATH, value="//a[@class='contacts_link h4']")
print(hillel_email.get_attribute('href'))

webdriver.quit()





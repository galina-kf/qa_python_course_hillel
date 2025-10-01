import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

webdriver = WebDriver()

webdriver.get("http://localhost:8000/dz.html")
time.sleep(2)

# navigate to the frame 1
frame_1 = webdriver.find_element(By.CSS_SELECTOR, value="iframe[id='frame1']")
print(frame_1.get_attribute('src'))

# switch to the layer iframe 1
webdriver.switch_to.frame(frame_1)

# enter the secret word
input_1 = webdriver.find_element(By.CSS_SELECTOR, value="input[id='input1']")
input_1.send_keys('Frame1_Secret')
time.sleep(2)

button_1 = webdriver.find_element(By.XPATH, value="//button")
button_1.click()

# check verifying alert and confirm
alert = Alert(webdriver)
print("Текст Prompt:", alert.text)
time.sleep(2)
alert.accept()

# return to the base page layer
webdriver.switch_to.default_content()

# navigate to the frame 2
frame_2 = webdriver.find_element(By.CSS_SELECTOR, value="iframe[id='frame2']")
print(frame_2.get_attribute('src'))

# switch to the layer iframe 2
webdriver.switch_to.frame(frame_2)

# enter the secret word
input_2 = webdriver.find_element(By.CSS_SELECTOR, value="input[id='input2']")
input_2.send_keys('Frame2_Secret')
time.sleep(2)

button_2 = webdriver.find_element(By.XPATH, value="//button")
button_2.click()

# check verifying alert and confirm
alert = Alert(webdriver)
print("Текст Prompt:", alert.text)
time.sleep(2)
alert.accept()

# return to the base page layer
webdriver.switch_to.default_content()

webdriver.quit()
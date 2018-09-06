from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/webdrivers/chromedriver.exe')

# open page
driver.implicitly_wait(15)
driver.get('http://mail.protonmail.com');

#login
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("SonyaP")
password.send_keys("SonyaP")
login_attempt = driver.find_element_by_id("login_btn")
login_attempt.submit()

#open compose window
wait = WebDriverWait(driver, 60)
compose = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sidebar-btn-compose")))
compose.click()

#compose message 
driver.switch_to_active_element()
driver.find_element_by_css_selector(".toRow input").send_keys("sonyapanich@gmail.com")
driver.find_element_by_css_selector(".subjectRow input").send_keys("Hello")

compose = driver.switch_to_frame(driver.find_element_by_css_selector(".squireIframe"))
msg_body = driver.find_element_by_css_selector(".protonmail_signature_block").get_attribute('innerHTML')
driver.execute_script("document.body.innerHTML = arguments[0]",  "Hello Sonya! How are you? It's been so long, we MUST hang out! See you soon!" + msg_body)
driver.switch_to_default_content()

#send message
driver.find_element_by_css_selector(".btnSendMessage-btn-action").click()

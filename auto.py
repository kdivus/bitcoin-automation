from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config

PATH = "/Windows/chromedriver"

driver = webdriver.Chrome(PATH)


driver.get("http://bitcoin.works")
driver.maximize_window()
driver.find_element_by_link_text("LOGIN").click()
driver.find_element_by_id("login_form_btc_address").send_keys(config.username)
driver.find_element_by_id("login_form_password").send_keys(config.password)
driver.find_element_by_id("login_button").click()
time.sleep(4)
driver.find_element_by_class_name("pushpad_deny_button").click()
time.sleep(7)
driver.find_element_by_class_name("play_without_captcha_button center").click()
driver.find_element_by_id("free_play_form_button").click()
time.sleep(3)
driver.quit()


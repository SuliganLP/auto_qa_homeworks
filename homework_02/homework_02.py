from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://itcareerhub.de/ru")
sleep(5)

payment_methods = driver.find_element(By.LINK_TEXT, "Способы оплаты")
payment_methods.click()
sleep(4)

driver.save_screenshot("./screenshot.png")

driver.quit()

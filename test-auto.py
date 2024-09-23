from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'https://only.digital/projects#brief'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
name = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/input")
name.send_keys('Ivanov')
time.sleep(3)
company = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div[1]/div/div[4]/div/input")
#email = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input"))
#)
company.send_keys('Рога и Копыта')
time.sleep(3)
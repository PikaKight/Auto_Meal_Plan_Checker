from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

def auto(user, psw):
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://mealplan.uwo.ca/Topup/Login")
    username = driver.find_element(By.ID, "Username")
    password = driver.find_element(By.ID, "Password")


    username.send_keys(user)
    password.send_keys(psw)

    driver.find_element(By.CLASS_NAME, "login_submit").find_element(By.XPATH, "//button[text()='Log In']").click()

    time.sleep(2)

    bal = driver.find_element(By.XPATH, "//td[text()[contains(., '$')]]").text
    print(bal)




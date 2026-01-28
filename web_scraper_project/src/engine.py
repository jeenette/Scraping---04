# src/engine.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    options = Options()
    options.add_argument("--headless")  # run in background
    options.add_argument("user-agent=Mozilla/5.0")
    
    # path to your chromedriver
    service = Service("C:/path/to/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login(driver, username, password):
    driver.get("https://www.bid4assets.com/login")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    
    # wait until logged in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))

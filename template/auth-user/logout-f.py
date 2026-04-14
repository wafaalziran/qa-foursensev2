from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))
    print(" Login berhasil")

    menu_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
    menu_button.click()
    logout = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
    print(" Error message:", error_message.text)
    
finally:
    time.sleep(3)
    driver.quit()
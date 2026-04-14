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

    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    print(f" Jumlah produk tampil: {len(products)}")

    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

    cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    print(" Cart count:", cart_badge.text)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Auto")
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("40123")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    success_message = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    print(" Order Status:", success_message.text)

    if "THANK YOU" in success_message.text.upper():
        print(" Order berhasil dibuat")
    else:
        print(" Order gagal")

finally:
    time.sleep(3)
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

users = [
    ("student@example.com", "password", "/student"),
    ("teacher@example.com", "password", "/teacher"),
    ("admin@example.com", "password", "/admin"),
]

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

for email, password, expected_url in users:
    try:
        driver.get("http://localhost:3000")

        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        wait.until(EC.url_contains(expected_url))
        print(f"[V] Login berhasil: {email}")

    except Exception as e:
        print(f"[X] Login gagal: {email} | Error: {str(e)}")

driver.quit()
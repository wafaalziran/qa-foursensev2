# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://localhost:3000")

    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
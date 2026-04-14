# pages/absence_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AbsencePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:3000/student/absence")

    def add_task(self, title):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@data-testid='btn-add-task']")
        )).click()

        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@data-testid='input-task-title']")
        )).send_keys(title)

        self.driver.find_element(
            By.XPATH, "//*[@data-testid='btn-save-task']"
        ).click()

    def check_task(self):
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@data-testid='checkbox-task']")
        )).click()

    def go_to_absence_tab(self):
        self.driver.find_element(
            By.XPATH, "//*[@data-testid='btn-tab-absence']"
        ).click()

    def do_absen(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@data-testid='btn-absen']")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@data-testid='btn-confirm-absen']")
        )).click()
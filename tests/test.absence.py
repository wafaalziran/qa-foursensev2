# tests/test_absence.py
from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.absence_page import AbsencePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_full_absence_flow():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        login = LoginPage(driver)
        absence = AbsencePage(driver)

        # LOGIN
        login.open()
        login.login("student@example.com", "password")

        wait.until(EC.url_contains("/student/dashboard"))

        # ABSENCE FLOW
        absence.open()
        absence.add_task("QA Automation Task")
        absence.check_task()
        absence.go_to_absence_tab()
        absence.do_absen()

        print("✅ FULL FLOW SUCCESS")

    finally:
        driver.quit()
import time
from pages.login_page import FormPage

def test_form_submission(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    form = FormPage(driver)

    form.fill_form("student", "Password123")
    form.submit()

    time.sleep(2)  # allow page to load

    assert "Logged In Successfully" in driver.page_source

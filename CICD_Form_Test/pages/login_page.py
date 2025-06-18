from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

    def submit(self):
        self.driver.find_element(By.ID, "submit").click()

from selenium.webdriver.common.by import By

class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self):
        self.driver.find_element(By.ID, "clickBtn").click()

    def get_heading_text(self):
        return self.driver.find_element(By.ID, "heading").text

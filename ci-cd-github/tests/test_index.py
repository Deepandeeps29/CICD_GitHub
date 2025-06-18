from pages.index_page import IndexPage
import os


def test_button_click(driver):
    filepath = os.path.abspath("index.html")
    driver.get(f"file://{filepath}")

    page = IndexPage(driver)
    assert page.get_heading_text() == "Welcome to CI/CD"

    page.click_button()
    assert page.get_heading_text() == "Button Clicked!"

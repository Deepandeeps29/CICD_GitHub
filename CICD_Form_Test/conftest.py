import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # For CI environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

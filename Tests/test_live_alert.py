from urllib.parse import urljoin
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_live_alert(driver: WebDriver):
    driver.get("http://127.0.0.1:5500/docs/messages/index.html")

    button_1 = driver.find_element(By.ID, "liveAlertTimeoutBtn")
    button_1.click()
    

    message_div = driver.find_element((By.CSS_SELECTOR, ".alert-success")).text
    message = message_div.text
    assert "Nice" in message

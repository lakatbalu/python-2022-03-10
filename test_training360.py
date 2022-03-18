from urllib.parse import urljoin
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_training_360_screenshot(driver: WebDriver):
    driver.get("https://www.training360.com/")
    driver.save_screenshot("main.png")

    newsletter_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "NewsletterModalCloseButton"))
    )
    newsletter_button.click()

    #driver.find_element(By.ID, "NewsletterModalCloseButton").click()

    driver.find_element(By.CSS_SELECTOR, ".cookie button").click()

    element = driver.find_element(By.CSS_SELECTOR, "[data-href='/irodai-informatika']")
    element.screenshot("informatika.png")

    title = driver.title
    assert "informatikai tanfolyamok" in title.lower()
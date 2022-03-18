from urllib.parse import urljoin
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#@pytest.fixture
#def get_url(driver: WebDriver):
#    driver.get("http://localhost:8080/")


def test_new_location(driver: WebDriver):
    driver.get("http://localhost:8080/")

    create_new_button = driver.find_element(By.ID, "create-location-link")
    create_new_button.click()

    driver.find_element(By.ID, "location-name").send_keys("Fonyód")
    driver.find_element(By.ID, "location-coords").send_keys("1,1")

    driver.find_element(By.CSS_SELECTOR, "#location-form > p > input.btn.btn-primary").click()

    #WebDriverWait(driver, 10).until(
    #    EC.visibility_of_element_located((By.ID, "NewsletterModalCloseButton"))
    #)
    message = driver.find_element(By.ID, "message-div").text
    assert "location has been created" in message.lower()

def test_delete_location(driver: WebDriver):
    driver.get("http://localhost:8080/")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "locations-table"))
    )

    delete_button1 = driver.find_element(By.CSS_SELECTOR, "#locations-table-tbody > tr:nth-child(3) > td:nth-child(6) > button.btn.btn-danger")
    delete_button1.click()

    delete_message1 = driver.find_element(By.CSS_SELECTOR, "#delete-location-form > p:nth-child(1)").text
    assert "are you sure" in delete_message1.lower()

    delete_button2 = driver.find_element(By.CSS_SELECTOR, "#delete-location-form > p:nth-child(3) > input.btn.btn-danger")
    delete_button2.click()

    delete_message2 = driver.find_element(By.ID, "message-div").text
    assert "location has been deleted" in delete_message2.lower()


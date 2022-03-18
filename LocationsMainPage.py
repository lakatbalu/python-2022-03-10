from lib2to3.pgen2 import driver
from urllib.parse import urljoin
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LocationsMainPage:

    def __init__(self, driver) -> None:
        self.driver = driver


    def open(self):
        self.driver.get("http://localhost:8080")

    def click_create_location_link(self):

        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Create Location")))
        
        create_new_button = self.driver.find_element(By.ID, "create-location-link")
        create_new_button.click()

    def fill_form(self, name: str = "Home", coords: str = "1,1", interesting_at: str = "2019-09-17T05:00:00", tags: str = "test"):   #default érték megadás
       loc_name =  self.driver.find_element(By.ID, "location-name")
       loc_name.send_keys(name)

       loc_coords = self.driver.find_element(By.ID, "location-coords")
       loc_coords.send_keys(coords)

       loc_interesting = self.driver.find_element(By.ID, "location-interesting-at")
       loc_interesting.send_keys(interesting_at)

       loc_tag = self.driver.find_element(By.ID, "location-tags")
       loc_tag.send_keys(tags)

    def click_on_create_location_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#location-form > p > input.btn.btn-primary").click()

    def assert_text_on_message_panel(self, text):
        message_div = self.driver.find_element(By.ID, "message-div")
        assert message_div.text == text

    def assert_error_message(self, text):
         message_div = self.driver.find_element(By.CSS_SELECTOR, ".invalid-feedback:not([hidden ='hidden'])")
         assert message_div.text == text


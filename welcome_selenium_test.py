from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def go_to_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/Docs/index.html")
    return driver

def fill_input_field(driver, name):
    driver.find_element(By.ID, "name-input").send_keys(name)   
       

def click_on_button(driver):
    driver.find_element(By.ID, "submit-button").click()


def get_name(driver):
    content = driver.find_element(By.ID, "message-p").text
    return content

def test_say_hello():
    driver = go_to_page()
    fill_input_field(driver, "John Doe")
    click_on_button(driver)
    content = get_name(driver)
    print(content)
    assert content == "Hello John Doe!" 


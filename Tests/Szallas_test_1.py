from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://szallas.hu/kereses/egyszeru?search=")
driver.find_element(By.ID, "location_header_input").send_keys("Fonyód")
driver.find_element(By.ID, "header_search_button").click()
print("end")

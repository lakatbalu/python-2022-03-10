
from sqlite3 import DatabaseError
from LocationsMainPage import LocationsMainPage
import requests
import mariadb


def test_create(driver):
    
    #requests.delete("http://localhost:8080/api/locations")

    conn = mariadb.connect(user="location",password="locations", host="localhost", database="locations")
    cur = conn.cursor()
    cur.execute("delete from locations")

    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form()
    page.click_on_create_location_button()
    page.assert_text_on_message_panel("Location has been created")
    print("end")

def test_empty_coords(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(name = "")
    page.click_on_create_location_button()
    page.assert_error_message("Can not be empty name!")
    print("end")

def test_empty_name(driver):
    page = LocationsMainPage(driver)
    page.open()
    page.click_create_location_link()
    page.fill_form(coords = "")
    page.click_on_create_location_button()
    page.assert_error_message("Invalid format!")
    print("end")


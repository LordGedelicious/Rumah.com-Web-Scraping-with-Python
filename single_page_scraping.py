from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from helper import *

# Order of the file contained in the results list:
# 1. Property Name (Nama Properti)
# 2. Property Price (Harga Properti)
# 3. Number of bedrooms (Jumlah Kamar Tidur)
# 4. Number of bathrooms (Jumlah Kamar Mandi)
# 5. Price per meter squared (Harga per meter persegi)
# 6. Property Type (Tipe Properti)
# 7. Property's Land Area (Luas Tanah Properti)
# 8. Property's Building Area (Luas Bangunan Properti)
# 8. Property's Interior (Interior Properti)
# 9. Number of Floors (Jumlah Lantai)
# 10. Parking Spaces (Jumlah Tempat Parkir)
# 11. Property's Year of Construction (Tahun Konstruksi Properti)
# 12. Property's Listing Date (Tanggal Listing Properti)
# 13. Property's Latitude (Latitude Properti)
# 14. Property's Longitude (Longitude Properti)
# 15. Property's Developer (Pengembang Properti)
# 14. Property's Description (Deskripsi Properti)
# 15. URL to Property's Page (URL Properti)
results = []

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

page_link = "https://www.rumah.com/listing-properti/dijual-rumah-mewah-di-jakarta-harga-termurah-wisteria-keppeland-dekat-aeon-mal-ikea-akses-tol-oleh-meliana-20242752"

start_time = time.time()
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get(page_link)
randomSleepTime()
property_name = driver.find_element(
    By.XPATH, "//h1[@class='h2 text-transform-none']").text
property_price = driver.find_element(
    By.XPATH, "//span[@class='element-label price']").get_attribute("content")
property_bedroom_count = driver.find_element(
    By.XPATH, "//div[@class='property-info-element beds']").text
property_bathroom_count = driver.find_element(
    By.XPATH, "//div[@class='property-info-element baths']").text
property_information = driver.find_elements(
    By.XPATH, "//td[@class='value-block']")
property_type = property_information[0].text
property_land_area = property_information[1].text
property_developer = property_information[2].text
property_building_area = property_information[3].text
property_price_per_metersq = property_information[4].text
property_interiors = property_information[5].text
property_floor_count = property_information[6].text
property_construction_year = property_information[8].text
property_listing_date = property_information[11].text
property_parking_spaces = property_information[12].text
try:
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight / 2);")
    property_maps = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"maps.google.com")]'))).get_attribute("href")
    property_latitude, property_longitude = returnLatitudeLongitude(
        property_maps)
except:
    property_maps = "FAIL TO FIND MAPS LINK"
    property_latitude = "FAIL TO FIND LATITUDE"
    property_longitude = "FAIL TO FIND LONGITUDE"
end_time = time.time()
time_elapsed = end_time - start_time
print("Property Name: {}".format(property_name))
print("Property Price: {}".format(property_price))
print("Property Bedroom Count: {}".format(property_bedroom_count))
print("Property Bathroom Count: {}".format(property_bathroom_count))
print("Property Price Per Meter Squared: {}".format(
    property_price_per_metersq[3:-7]))
print("Property Type: {}".format(property_information[0].text))
print("Property Land Area: {} m^2".format(property_land_area[:-3]))
print("Property Building Area: {} m^2".format(property_building_area[:-3]))
print("Property Interiors: {}".format(property_interiors))
print("Property Floor Count: {}".format(property_floor_count))
print("Property Parking Spaces: {}".format(property_parking_spaces))
print("Property Construction Year: {}".format(property_construction_year))
print("Property Listing Date: {}".format(property_listing_date))
print("Property Latitude: {}".format(property_latitude))
print("Property Longitude: {}".format(property_longitude))
print("Property Developer: {}".format(property_developer))
print("Link to Maps: {}".format(property_maps))
print("Link to Property Page: {}".format(page_link))
print("Time Elapsed: {}".format(time_elapsed))

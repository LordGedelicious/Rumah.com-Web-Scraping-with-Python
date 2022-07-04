# First alternative : Using the requests module to access page

# import os
# import requests
# target_district = ["Cakung", "Kelapa Gading", "Cilincing"]
# target = target_district[0]
# url = "https://www.rumah.com/properti-dijual?freetext={}&listing_type=sale&market=residential&property_type=B&property_type_code[]=BUNG&listing_posted=31&search=true".format(
#     target)
# page = requests.get(url)

# print(page.text)

# First alternative results: FAILED, denied access

# -----------------------------------------------------------------

# Second Alternative: Using the Selenium module to access page and scrape information
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from helper import *

target_district = ["Cakung", "Kelapa Gading", "Cilincing"]
target = target_district[0]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://www.rumah.com/properti-dijual?freetext={}&listing_type=sale&market=residential&property_type=B&property_type_code[]=BUNG&listing_posted=31&search=true".format(target))
randomSleepTime()

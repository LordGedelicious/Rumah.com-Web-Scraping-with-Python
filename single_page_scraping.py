from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from helper import *

# target_district = ["Cakung", "Kelapa Gading", "Cilincing"]
# target = target_district[0]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get(
    "https://www.rumah.com/listing-properti/dijual-cakung-oleh-zulfikar-20183527")
randomSleepTime()
property_name = driver.find_element(
    By.XPATH, "//h1[@class='h2 text-transform-none']").text
print(property_name)

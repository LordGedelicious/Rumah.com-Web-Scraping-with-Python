from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver.v2 as uc
import time
import pandas as pd
from helper import *
import csv
import random
import re


def randomSleepTime():
    random_time = random.randint(5, 10)
    time.sleep(random_time)


def returnLatitudeLongitude(maps_link):
    pattern_longitude = r'll=[-?\d\.]*\,([-?\d\.]*)'
    pattern_latitude = r'll=(-?[\d\.]*)'

    latitude = "".join(re.findall(pattern_latitude, maps_link))
    longitude = "".join(re.findall(pattern_longitude, maps_link))

    return latitude, longitude


def returnLinks(location_param, filename, max_page_limit):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-dev-shm-usage")
    results = []
    total_links = 0
    current_file_count = 0
    current_web_page_number = 1
    isLinkValid = True
    while isLinkValid:
        local_total_links = 0
        output_csv_filename = "{}_links_{}.csv".format(
            filename, current_file_count)
        with open(output_csv_filename, "a+", newline='') as f:
            writer = csv.writer(f)
            while True:
                if current_web_page_number > max_page_limit:
                    isLinkValid = False
                    break
                if current_web_page_number == 1:
                    page_link = "https://www.rumah.com/properti-dijual?freetext={}&listing_type=sale&listing_posted=31&property_type=B&property_type_code[]=BUNG&market=residential&search=true".format(
                        location_param)
                else:
                    page_link = "https://www.rumah.com/properti-dijual/{}?freetext={}&listing_type=sale&listing_posted=31&property_type=B&property_type_code[]=BUNG&market=residential&search=true".format(
                        current_web_page_number, location_param)
                randomSleepTime()
                driver = webdriver.Chrome(service=Service(
                    ChromeDriverManager().install()), options=options)
                # driver = uc.Chrome(options=options, version_main=97)
                driver.get(page_link)
                randomSleepTime()
                page_links = driver.find_elements(
                    By.XPATH, "//a[@class='nav-link']")
                for i in page_links:
                    temp_link = i.get_attribute("href")
                    if temp_link not in results:
                        results.append(temp_link)
                        local_total_links += 1
                        total_links += 1
                        writer.writerow([temp_link])
                print("Successfully added links from page {} for search {}".format(
                    current_web_page_number, location_param))
                current_web_page_number += 1
    print("{} links written in total.".format(total_links))

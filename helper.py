from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import undetected_chromedriver.v2 as uc
import time
import pandas as pd
from helper import *
import csv
import random
import re


def noteFailure(url):
    with open("failed_urls.txt", "a") as f:
        f.write(url + "\n")
        f.close()


def randomSleepTime():
    random_time = random.randint(3, 7)
    time.sleep(random_time)


def returnLatitudeLongitude(maps_link):
    pattern_longitude = r'll=[-?\d\.]*\,([-?\d\.]*)'
    pattern_latitude = r'll=(-?[\d\.]*)'

    latitude = "".join(re.findall(pattern_latitude, maps_link))
    longitude = "".join(re.findall(pattern_longitude, maps_link))

    return latitude, longitude


def processResults(results):
    if results[11] != 'N/A':
        try:
            new_construction_date = results[11].replace(", ", " ")
            new_construction_datetime = datetime.strptime(
                new_construction_date, '%B %Y')
            results[11] = new_construction_datetime.strftime('%Y-%m-%d')
        except:
            new_construction_date = results[11].replace(", ", " ")
            new_construction_datetime = datetime.strptime(
                new_construction_date, '%Y')
            results[11] = new_construction_datetime.strftime('%Y-%m-%d')
    if results[12] != 'N/A':
        base_text = results[12]
        if "jam" in base_text:
            remainder = base_text[:-14]
            datetime_object = datetime.now() - timedelta(hours=int(remainder))
        elif "hari" in base_text:
            remainder = base_text[:-15]
            datetime_object = datetime.now() - timedelta(days=int(remainder))
        elif "minggu" in base_text:
            remainder = base_text[:-17]
            datetime_object = datetime.now() - timedelta(days=7*int(remainder))
        elif "bulan" in base_text:
            remainder = base_text[:-16]
            datetime_object = datetime.now() - timedelta(days=30*int(remainder))
        # print(datetime_object)
        results[12] = datetime_object.strftime('%Y-%m-%d')
    for index in range(len(results)):
        if results[index] == 'N/A':
            results[index] = None
    return results


def returnLinks(location_param, filename, max_page_limit):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--disable-dev-shm-usage")
    # options = Options()
    # options.add_argument("--disable-dev-shm-usage")
    results = []
    total_links = 0
    current_file_count = 0
    current_web_page_number = 113
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
                driver = webdriver.Edge(
                    executable_path=r"C:\Users\Gede Prasidha\Downloads\edgedriver_win64\msedgedriver.exe")
                # driver = webdriver.Chrome(service=Service(
                #     ChromeDriverManager().install()), options=options) [ USE FOR INDIVIDUAL WEB SCRAPING ]
                # driver = uc.Chrome(options=options, version_main=97)
                driver.get(page_link)
                time.sleep(random.randint(7, 10))
                time.sleep(random.randint(7, 10))
                print("You should've completed the CAPTCHA by now, otherwise repeat from page {}".format(
                    current_web_page_number))
                page_links = driver.find_elements(
                    By.XPATH, "//a[@class='nav-link']")
                randomSleepTime()
                for i in page_links:
                    temp_link = i.get_attribute("href")
                    if temp_link not in results:
                        results.append(temp_link)
                        local_total_links += 1
                        total_links += 1
                        writer.writerow([temp_link])
                print("Successfully added {} links from page {} for search {}".format(
                    len(results), current_web_page_number, location_param))
                current_web_page_number += 1
                driver.close()
    print("{} links written in total.".format(total_links))


def returnDataFromIndividualLink(page_link, searched_district):
    results = []

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--disable-dev-shm-usage")

    start_time = time.time()
    driver = webdriver.Edge(
        executable_path=r"C:\Users\Gede Prasidha\Downloads\edgedriver_win64\msedgedriver.exe")
    driver.get(page_link)
    randomSleepTime()
    canAccessDetails = True
    try:
        property_name = driver.find_element(
            By.XPATH, "//h1[@class='h2 text-transform-none']").text
    except:
        property_name = "N/A"
    try:
        property_price = driver.find_element(
            By.XPATH, "//span[@class='element-label price']").get_attribute("content")
    except:
        property_price = "N/A"
    try:
        property_bedroom_count = driver.find_element(
            By.XPATH, "//div[@class='property-info-element beds']").text
    except:
        property_bedroom_count = "N/A"
    try:
        property_bathroom_count = driver.find_element(
            By.XPATH, "//div[@class='property-info-element baths']").text
    except:
        property_bathroom_count = "N/A"
    try:
        property_information = driver.find_elements(
            By.XPATH, "//td[@class='value-block']")
    except:
        canAccessDetails = False
    if canAccessDetails:
        property_type = property_information[0].text
        property_land_area = property_information[1].text
        property_developer = property_information[2].text
        property_building_area = property_information[3].text
        property_price_per_metersq = property_information[4].text
        property_interiors = property_information[5].text
        property_floor_count = property_information[6].text
        property_construction_date = property_information[8].text
        property_listing_date = property_information[11].text
    else:
        property_type = "N/A"
        property_land_area = "N/A"
        property_developer = "N/A"
        property_building_area = "N/A"
        property_price_per_metersq = "N/A"
        property_interiors = "N/A"
        property_floor_count = "N/A"
        property_construction_date = "N/A"
        property_listing_date = "N/A"
    try:
        property_parking_spaces = property_information[12].text
    except:
        property_parking_spaces = 'N/A'
    try:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight / 2);")
        property_maps = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"maps.google.com")]'))).get_attribute("href")
        property_latitude, property_longitude = returnLatitudeLongitude(
            property_maps)
    except:
        property_maps = 'N/A'
        property_latitude = 'N/A'
        property_longitude = 'N/A'
    end_time = time.time()
    time_elapsed = end_time - start_time
    results.append(property_name)
    results.append(property_price)
    results.append(property_bedroom_count)
    results.append(property_bathroom_count)
    results.append(property_price_per_metersq[3:-7])
    results.append(property_type)
    results.append(property_land_area[:-3])
    results.append(property_building_area[:-3])
    results.append(property_interiors)
    results.append(property_floor_count)
    results.append(property_parking_spaces)
    results.append(property_construction_date)
    results.append(property_listing_date)
    results.append(property_latitude)
    results.append(property_longitude)
    results.append(property_maps)
    results.append(property_developer)
    results.append(page_link)
    # print(results)
    results2 = processResults(results)
    driver.close()
    # print(results2)
    return time_elapsed, results2
    # print("Property Name: {}".format(property_name))
    # print("Property Price: {}".format(property_price))
    # print("Property Bedroom Count: {}".format(property_bedroom_count))
    # print("Property Bathroom Count: {}".format(property_bathroom_count))
    # print("Property Price Per Meter Squared: {}".format(
    #     property_price_per_metersq[3:-7]))
    # print("Property Type: {}".format(property_information[0].text))
    # print("Property Land Area: {} m^2".format(property_land_area[:-3]))
    # print("Property Building Area: {} m^2".format(property_building_area[:-3]))
    # print("Property Interiors: {}".format(property_interiors))
    # print("Property Floor Count: {}".format(property_floor_count))
    # print("Property Parking Spaces: {}".format(property_parking_spaces))
    # print("Property Construction Year: {}".format(property_construction_year))
    # print("Property Listing Date: {}".format(property_listing_date))
    # print("Property Latitude: {}".format(property_latitude))
    # print("Property Longitude: {}".format(property_longitude))
    # print("Property Developer: {}".format(property_developer))
    # print("Link to Property Page: {}".format(page_link))


# latitude, longitude = returnLatitudeLongitude(
#     "https://maps.google.com/maps?ll=-6.367401,106.65508&z=16&t=m&hl=en-US&gl=US&mapclient=apiv3")
# print(latitude, longitude)

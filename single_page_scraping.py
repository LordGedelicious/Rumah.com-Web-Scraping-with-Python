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

# For complete csv links:
df = pd.read_csv("kelapa gading_links.csv", header=None)
file_length = len(df)
total_time = 0
# returnDataFromIndividualLink(df[0][0], "cilincing")
with open("kelapa gading_data.csv", "a+", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for idx in range(1299, len(df), 1):
        try:
            process_time, temp_results = returnDataFromIndividualLink(
                df[0][idx], "kelapa gading")
            writer.writerow(temp_results)
            print(
                "Successfully wrote data number {} to kelapa gading_data.csv".format(idx+1))
            total_time += process_time
        except:
            noteFailure(df[0][idx])
            print(
                "Failed to write data number {} to kelapa gading_data.csv".format(idx+1))
            continue
print("Successfully extracted data from cilincing_links.csv")
print("Average process time: {}".format(total_time/file_length))
print("Total process time: {}".format(total_time))

# For individual links:
# with open("cilincing_data.csv", "a+", newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     page_link = "https://www.rumah.com/listing-properti/dijual-dijual-rumah-full-renov-siap-huni-di-alamanda-jakarta-garden-city-jgc-oleh-lusia-ester-17523546"
#     process_time, temp_results = returnDataFromIndividualLink(
#         page_link, "cilincing")
#     writer.writerow(temp_results)
#     print("Successfully wrote data manually to cilincing_data.csv")

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
import csv
import random

results = []

page_num_limit_list = [140, 156, 40]
districts = ["kelapa+gading", "cakung", "cilincing"]
district_names = ["kelapa gading", "cakung", "cilincing"]

returnLinks(districts[0], district_names[0], page_num_limit_list[0])
# random_time = random.randint(10, 20)
# time.sleep(random_time)
# try:
#     returnLinks(districts[1], district_names[1], page_num_limit_list[1])
# except:
#     print("Error in {}\n\n".format(district_names[1]))
# random_time = random.randint(10, 20)
# time.sleep(random_time)
# try:
#     returnLinks(districts[2], district_names[2], page_num_limit_list[2])
# except:
#     print("Error in {}\n\n".format(district_names[2]))

import random
import time
import re


def randomSleepTime():
    random_time = random.randint(3, 10)
    time.sleep(random_time)


def returnLatitudeLongitude(maps_link):
    pattern_longitude = r'll=[-?\d\.]*\,([-?\d\.]*)'
    pattern_latitude = r'll=(-?[\d\.]*)'

    latitude = "".join(re.findall(pattern_latitude, maps_link))
    longitude = "".join(re.findall(pattern_longitude, maps_link))

    return latitude, longitude

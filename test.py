import re

link = "https://maps.google.com/maps?ll=0.7893,113.9213&z=16&t=m&hl=en-US&gl=US&mapclient=apiv3"
pattern_longitude = r'll=[-?\d\.]*\,([-?\d\.]*)'
pattern_latitude = r'll=(-?[\d\.]*)'

latitude = "".join(re.findall(pattern_latitude, link))
longitude = "".join(re.findall(pattern_longitude, link))

print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))

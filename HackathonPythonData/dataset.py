import json
import random


hotel_name_array = {"H1", "H2", "H3", "H4", "H5", "H6"}
month_array = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}

data = {}

for name in hotel_name_array:
   hotel = {}
   for month in month_array:
       hotel[month] = round(random.uniform(1,5),1)
   data[name] = hotel

print(data)

json_data = json.dumps(data)

with open('dataSetHotelRatings.json', 'w') as f:
  json.dump(json_data, f)

print(json_data)


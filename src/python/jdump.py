#!/usr/bin/env python3

# json parser
import json
from datetime import datetime
# Data
dic = { "Timestamp": datetime.now().strftime("%d %m %Y"),
        "dict": {
                   "field1": 50,
                   "field2": 30,
                   "field3": 11.5
               }
      }
# json dump file
filename = "test.json"

# creating json dump and dumping dictionary data
with open(filename, 'w', encoding = "utf-8") as file:
    json.dump(dic, file)

# loading json dump as dictionary
with open(filename, 'r', encoding = "utf-8") as file:
    lo = json.load(file)
print(lo)

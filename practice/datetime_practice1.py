#!/usr/bin/python3

import time
import datetime

today = datetime.date.today()
print("今天的日期: "+ str(today))

other_day = datetime.date(2016,11,15)
result = today - other_day
print(result)
print("只要天數: " + str(result.days))

print("Year:" + str(today.strftime("%Y")))
print("Month: " + str(today.strftime("%m")))
print("Day: " + str(today.strftime("%d")))


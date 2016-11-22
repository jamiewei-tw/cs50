#!/usr/bin/python3

import calendar
#import datetime
from datetime import timedelta
from datetime import date

while True:
    try:
        Year = input('Year: ')
        iYear = int(Year)
    
        if 1 <= iYear <= 10000:
            break
        else:
            print("Please Enter A Number Between 1 to 10000")
    except:
        print("Please Enter A Number")
        


while True:
    try:
        Month = input('Month:')
        iMonth = int(Month)
        
        if 1 <= iMonth <= 12:
            break
        else:
            print ("Please Enter A Number Between 1 to 12")
    except:
        print("Please Enter A Number")
   

if iMonth == 1:
   Month = "    January "
   
elif iMonth == 2:
   Month = "    Febuary "

elif iMonth == 3:
   Month = "    March "
   
elif iMonth == 4:
   Month = "    April "
   
elif iMonth == 5:
   Month = "    May "
   
elif iMonth == 6:
   Month = "    June "
   
elif iMonth == 7:
   Month = "    July "
   
elif iMonth == 8:
   Month = "    August "

elif iMonth == 9:
   Month = "    September "

elif iMonth == 10:
   Month = "    October "

elif iMonth == 11:
   Month = "    November "
   
else:
   Month = "    December "

Month = Month + Year
print(Month)
   

print(" SUN MON TUE WED THU FRI SAT")

Dt1 = date(iYear,iMonth,1)
WDt1 = date.weekday(Dt1) + 1

Weekday_list = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

def printDate(x):
    OutPut = ''
    for i in range (0,x):
        OutPut = OutPut + str(Weekday_list[i])
    return OutPut
        

if WDt1 == 7:
    Weekday_list[0] = 1
    
if WDt1 == 1:
    Weekday_list[2] = 1
        
if WDt1 == 2:
    Weekday_list[4] = 1
            
if WDt1 == 3:
    Weekday_list[6] = 1
    
if WDt1 == 4:
    Weekday_list[8] = 1
        
if WDt1 == 5:
    Weekday_list[10] = 1
    
if WDt1 == 6:
    Weekday_list[12] = 1

PD = printDate(13)
print(PD)

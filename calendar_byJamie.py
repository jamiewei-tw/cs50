#!/usr/bin/python3

import calendar
import datetime
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
  
Dt1 = date(iYear,iMonth,1)                
WDt1 = date.weekday(Dt1) + 1                 # Get the first weekday of the month

Last_Day = calendar.monthrange(iYear, iMonth)
iDay = Last_Day[1]
DtL = date(iYear, iMonth, iDay)        # Get the last date of the month
WDtL = date.weekday(DtL)+1             # Get the last weekday of the month


Month = calendar.month_name[iMonth] + " " + Year
print(Month.center(28))
   
print(" SUN MON TUE WED THU FRI SAT")


Numbers = [7, 1, 2, 3, 4, 5, 6]
N = 0
End = ''
for F in range(0,7):                         # 'F' for the first day of the month
    if WDt1 == Numbers[F]:
        print(str(1).rjust(4),end='')
        N += 1
        break
    else:
        Empty = ''
        print(Empty.rjust(4),end='')
        N += 1

for L in range(2, iDay+1):
    if N == 6:
        print(str(L).rjust(4))
        N = 0
        
    else:
        print(str(L).rjust(4), end='')
        N += 1
        
print(End)

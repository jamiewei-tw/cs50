#!/usr/bin/python3
Year = input('Year: ')
if 1 <= Year <= 10000:
    Year_int = int(Year)
else:
    print "Please Enter A Number Between 1 to 10000"
  
Month = input('Month:')
if 1 <= Month <= 12:
    Month_int = int(Month)
else:
    print "Please Enter A Number Between 1 to 12"
   

calendar = []

def Fcalendar(x,y):
    calendar.append(x)
    calendar.append(y)
    return calendar

Ocalendar = Fcalendar(Year_int, Month_int)
print(Ocalendar)

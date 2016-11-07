#!/usr/bin/python3
Year = input('Year: ')
Month = input('Month:')
Year_int = int(Year)
Month_int = int(Month)
calendar = []

def Fcalendar(x,y):
    calendar.append(x)
    calendar.append(y)
    return calendar

Ocalendar = Fcalendar(Year_int, Month_int)
print(Ocalendar)
    

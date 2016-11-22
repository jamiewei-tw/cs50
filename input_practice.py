#!/usr/bin/python3

import calendar

while True:
    try:
        Year = int(input('Year: '))
    
        if 1 <= Year <= 10000:
            break
        else:
            print("Please Enter A Number Between 1 to 10000")
    except:
        print("Please Enter A Number")


while True:
    try:
        Month = int(input('Month:'))
        
        if 1 <= Month <= 12:
            break
        else:
            print ("Please Enter A Number Between 1 to 12")
    except:
        print("Please Enter A Number")
   

Fcal = []

def Fcalendar(x,y):
    Fcal.append(x)
    Fcal.append(y)
    return Fcal
    
    
Ocalendar = Fcalendar(Year, Month)
cal = calendar.month(Year, Month)

print(Ocalendar)
print(cal)

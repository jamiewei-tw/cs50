#!/usr/bin/python3


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
   

calendar = []

def Fcalendar(x,y):
    calendar.append(x)
    calendar.append(y)
    return calendar

Ocalendar = Fcalendar(Year, Month)
print(Ocalendar)

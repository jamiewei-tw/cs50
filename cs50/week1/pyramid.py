#!/usr/bin/python3

def checktheword(N):
    try:
        N = int(N)
        if N >= 1:
            return N
    
        elif N<= 0:
            print("Please Input A Number Larger than 0")
            number = checktheword(input("Input a number: "))
            return number
            
    except:
        print("Please Input An Number")
        number = checktheword(input("Input a number: "))
        return number

number = checktheword(input("Input a number: "))
Pyramid = ''


for P in range(1, number+1):
    Pyramid = Pyramid + '#'
    print(Pyramid.rjust(number), end='')
    print(' ', end='')
    print(Pyramid.ljust(number))

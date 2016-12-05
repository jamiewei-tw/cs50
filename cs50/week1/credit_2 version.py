#!/usr/bin/python3

def Checktheenter(N):
    try:
        N = int(N)
        return N
           
    except:
        print("**Please Enter Only Numbers**")
        CreditNum = Checktheenter(input("Please Enter YOur Credit Number: "))
        return CreditNum


def CreditSum(CS):
    Length = len(CS)
    Sum = 0
    CS_Double = 0
    
    if Length % 2 == 0:
        for C in range(1,Length, 2):
            Sum = Sum + int(CS[C])
            
        for C in range(0, Length, 2):
            CS_Double = int(CS[C]) * 2
            
            if CS_Double <= 9:
                Sum = Sum + CS_Double
                
            else: 
                CS_Double2 = str(CS_Double)
                CS_Double2_Sum = int(CS_Double2[0]) + int(CS_Double2[1])
                Sum = Sum + CS_Double2_Sum

    else:
        for C in range(0,Length, 2):
            Sum = Sum + int(CS[C])
            
        for C in range(1, Length, 2):
            CS_Double = int(CS[C]) * 2
            
            if CS_Double <= 9:
                Sum = Sum + CS_Double
                
            else: 
                CS_Double2 = str(CS_Double)
                CS_Double2_Sum = int(CS_Double2[0]) + int(CS_Double2[1])
                Sum = Sum + CS_Double2_Sum
          
    return Sum


def Check(Sum, Num):
    length = len(Num)
    Card_Num = int(Num[0] + Num[1])
    if Sum % 10 == 0:
        if length == 15:
            if Card_Num == 34 or Card_Num == 37:
                print("AMEX")
                
            else:
                print("INVALID")    
                
        elif length == 16:
            if 51 <= Card_Num <= 55:
                print("MASTER")
                
            elif Num[0] == '4':
                print("VISA")
                
            else:
                print("INVALID")
            
        elif length == 13:   
            if Num[0] == '4':
                print("VISA")
            
            else:
                print("INVALID")
                 
        else:
            print("INVALID")
            
    else:
        print("INVALID")


CreditNum = Checktheenter(input("Please Enter YOur Credit Number: "))
CreditNum = str(CreditNum)

Credit_Sum = CreditSum(CreditNum)
A = "Number: " + CreditNum
print(A)
Check = Check(Credit_Sum, CreditNum)
   
    


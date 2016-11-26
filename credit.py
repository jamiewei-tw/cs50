#!/usr/bin/python3

def Checktheenter(N):
    try:
        N = int(N)
        if N >= 1000000000000000:
            N = str(N)
            return N
       
        else:
            print("**Please Enter the 16 Numbers of the Credit Card**")
            CreditNum = Checktheenter(input("Please Enter YOur Credit Number: "))
            return CreditNum
           
    except:
        print("**Please Enter Only Numbers**")
        CreditNum = Checktheenter(input("Please Enter YOur Credit Number: "))
        return CreditNum


def CreditSum(CS):
    Sum = 0
    CS_Double = 0
    
    for C in range(0,16):
        if C == 1 or C == 3 or C == 5 or C == 7 or C == 9 or C == 11 or C == 13 or C == 15:
            Sum = Sum + int(CS[C])
        
        else: 
            CS_int = int(CS[C])
            CS_int_Double = CS_int * 2
            if CS_int_Double <= 9:
                Sum = Sum + CS_int_Double
            
            else: 
                CS_Double = str(CS_int_Double)
                CS_Double_Sum = int(CS_Double[0]) + int(CS_Double[1])
                Sum = Sum + CS_Double_Sum
            
    return Sum


def Check(Sum):
    if Sum % 10 == 0:
        print("This Is A Credit Card")
        
    else:
        print("This Is Not A Credit Card")



CreditNum = Checktheenter(input("Please Enter YOur Credit Number: "))

Credit_Sum = CreditSum(CreditNum)
Check = Check(Credit_Sum)
        
        



    
    


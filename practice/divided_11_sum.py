sum11 = 0
sum13 = 0

for i in range(1,101):
    if i % 11 == 0 :
        print i
        sum11 = sum11 + i

    elif i % 13 == 0:
        print i 
        sum13 = sum13 + i

print sum11
print sum13

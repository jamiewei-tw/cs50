i = 1
sum11 = 0
sum13 = 0

while i <= 100:
    if i % 11 == 0 :
        print i
        sum11 = sum11 + i

    elif i % 13 == 0:
        print i
        sum13 = sum13 + i
    i += 1

print sum11
print sum13

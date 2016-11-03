isum = 0
for i in range(1,101):
    if i % 11 == 0 or i % 13 == 0:
        print i
        isum = isum + i

print isum

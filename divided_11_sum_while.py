i = 1
isum = 0

while i <= 100:
    if i % 11 == 0 or i % 13 == 0:
        print i
        isum = isum + i
    i += 1

print isum

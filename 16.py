from math import floor

s = 0
for i in range(400):
    s += floor( pow(2, 1000, 10**i) / 10**(i-1) )

print (s)

import math
n=600851475143

i=2
m=1

while i<= n:
    if n%i == 0:
        m=i
        n=n/i
    else: i=i+1

print(m)

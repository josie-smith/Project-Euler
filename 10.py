from math import *
p=[2]

for n in range(3,2000000):
    for x in p:
        if n%x==0:
            break
    else: p.append(n)

print(sum(p))

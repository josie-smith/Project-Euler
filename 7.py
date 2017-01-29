import math

def checkprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            p=False
            break
    else: p=True

    return p

c=1
i=2
while c<10001:
    i=i+1
    if checkprime(i):
        c=c+1
        P=i

print(P)

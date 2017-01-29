from useful import *

n=1
L=listprimes(10000)
T=lambda n: int(n*(n+1)/2)

if n%2==0:
    C1=countfacL(n/2,L)
    C2=countfacL(n+1,L)
    C=[C1[0],C2[0]]
    L=C2[1]
else:
    C1=countfacL(n,L)
    C2=countfacL((n+1)/2,L)
    C=[C1[0],C2[0]]
    L=C2[1]
    
while C[0]*C[1]<=500:
    n+=1
    C[0]=C[1]
    if n%2==0:
        C1=countfacL(n+1,L)
        C[1]=C1[0]
        L=C1[1]
    else:
        C1=countfacL((n+1)/2,L)
        C[1]=C1[0]
        L=C1[1]

print(T(n))

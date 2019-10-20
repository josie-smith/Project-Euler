from math import *
from functools import *
import time

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print ('func:%r args:[%r, %r] took: %2.4f sec') % \
          (f.__name__, args, kw, te-ts)
        return result
    return timed


# lists primes up to n

# @timeit - this will time this function
def listprimes(N):
    P=[True]*N
    P[0]=False
    P[1]=False
    n=2
    primes=[]
    while n<N:
        if P[n]:
            primes.append(n)
            i=n**2
            while i<N:
                P[i]=False
                i+=n
        n+=1
    return primes

# a generator function for primes n to infinity
def get_primes(number):
    while True:
        if checkprime(number):
            yield number
        number += 1
        # eg to iterate:
        # for next_prime in get_primes(3): ...


# checks whether a number is prime

def checkprime(n):
    K=listprimes(int(sqrt(n)))
    for i in K:
        if n%i==0:
            return False
            break
    else: return True


# prime factorisation of a number

def fac(n):
    P = []
    I = listprimes(int(sqrt(n))+1)
    i=0
    while I[i]*I[i] <= n:
        while n%I[i]==0:
            n //= I[i]
            P.append(I[i])
        i+=1
    if n>1:
        P.append(n)
    return P


# prime factorisation of a number without regenerating list of primes

def facL(n,L):
    if len(L)==0:
        L=[2]
    k=L[-1]+1
    while k*k<=n:
        for i in L:
            if k%i==0:
                break
        else:
            L.append(k)
        k+=1
    P = []
    i=0
    while L[i]*L[i] <= n:
        while n%L[i]==0:
            n //= L[i]
            P.append(L[i])
        i+=1
    if n>1:
        P.append(n)
    return P,L


#counts factors of a number

def countfac(n): 
    if n==1:
        return 1
    else:
        P=fac(n)
        d={x:P.count(x) for x in P}
        v=list(d.values())
        c=reduce(lambda x, y: x * y, [x+1 for x in v])
    return c


# counts factors of a number without regenerating list of primes

def countfacL(n,L):
    if n==1:
        return 1,L
    else:
        P=facL(n,L)
        d={x:P[0].count(x) for x in P[0]}
        v=list(d.values())
        c=reduce(lambda x, y: x * y, [x+1 for x in v])
    return c,L

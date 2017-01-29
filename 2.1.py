f=lambda x: 1 if x==0 else 1 if x==1 else f(x-1)+f(x-2)
N=largest i for which f(i)<=4000000
A=list(map(f,range(1,N+1)))
E=sum(Even=list(filter(lambda x: x%2==0,A)))

print(E)

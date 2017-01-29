
for b in range(1,1000):
    for a in range(1,b):
        S=1000*(1000-2*a-2*b)+2*a*b
        if S==0:
            print(a*b*(1000-a-b))
            break

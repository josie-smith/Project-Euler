f=[1,1]
i=2

# f is a list of fibonacci numbers

while f[i-1]+f[i-2]<=4000000:
    f.append(f[i-1]+f[i-2])
    i=i+1

s=0
for i in range(1, len(f)):
    if f[i]%2 == 0:
        s=s+f[i]

print(s)

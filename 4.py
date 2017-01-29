m=0
for i in range (100, 1000):
    for j in range(i, 1000):
        if str(i*j) == str(i*j)[::-1]:
            m=max(m,i*j)

print(m)

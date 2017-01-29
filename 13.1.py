A = []
with open('13.txt') as inputfile:
    for line in inputfile:
        A.append(int(line))

S=str(sum(A))
print(S[0:10])

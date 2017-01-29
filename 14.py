
def cNext(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n+1

def Collatz(n):
    checked = [0]*(n+1)
    longest = 1
    longestLength = 1

    for i in range(n, 1, -1):
        if checked[i] == 0:
            length = 1
            j = i

            while j != 1:
                j = cNext(j)
                if j < i:
                    checked[j] = 1
                length += 1
            if length > longestLength:
                longestLength = length
                longest = i
            # checked[i] = 1

    return longest
            
                
print(Collatz(1000000))

from math import sqrt

def check(pair):
    s = pair[0]
    t=pair[1]
    if (t-s)%2 == 1:
        m = t*t - s*s
        n = 2*s*t
        a = abs(m*m - n*n)
        b = 2*m*n
        c = sqrt(a*a + b*b)
        if c == int(c) and c <= 10**16:
            if (a*b)%84 != 0:
                return True
    return False

def farey( n ):
#    "Python function to print the nth Farey sequence, either ascending or descending."
    listofst = []
    count = 0
    a, b, c, d = 0, 1,  1 , n
    while c <= n:
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        # adds to the count only if it passes the check
        if check((a,b)): count +=1
    return count


print(farey(10**4))

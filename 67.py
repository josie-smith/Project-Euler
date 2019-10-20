triangle = []
f = open("67.txt", "r")
for line in f.readlines() :
    triangle.append( list(map(int, line.strip('\n').split(' ') )) )
f.close()

def triMax(triangle):
    length = len(triangle)
    sum = [[0]*length for x in range(length) ]

    for i in range(length) :
        for j in range(i+1) :
            if i == 0 :
                sum[i][j] = triangle[i][j]
            elif j == 0 :
                sum[i][j] = sum[i-1][j]+triangle[i][j]
            elif j == i :
                sum[i][j] = sum[i-1][j-1]+triangle[i][j]
            else :
                sum[i][j] = max( sum[i-1][j-1]+triangle[i][j] , sum[i-1][j]+triangle[i][j] )
    return max(sum[length-1])

print(triMax(triangle))

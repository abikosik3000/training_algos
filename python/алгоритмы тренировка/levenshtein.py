import math
def get_from_matr(matr , i , j  ):
    if(i == -1 and j == -1):
        return 0
    if(i >= n  or j >= m or i < 0 or j <0):
        return math.inf
    return matr[i][j]

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

s1 = fin.readline().rstrip()
s2 = fin.readline().rstrip()
m = len(s1) + 1
n = len(s2) + 1

matr = [  [0] * m  for i in range(n)]

for j in range(m ):
    matr[0][j] = j

for i in range(n ):
    matr[i][0] = i

for i in range(1,n):
    for j in range(1,m):
        matr[i][j] = min( matr[i - 1][j - 1] + int(s1[j - 1] != s2[i - 1]), 
                          matr[i - 1][j] + 1, 
                          matr[i][j - 1] + 1)

#for i in range(n):
#    print(matr[i])

fout.write( str(matr[n-1][m-1]) )

fout.close()
fin.close()
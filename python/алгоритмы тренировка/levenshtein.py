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
m = len(s1)
n = len(s2)


matr = [  [0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if(s1[j] == s2[i]):
            matr[i][j] += min( 
                get_from_matr(matr,i - 1, j - 1) ,
                get_from_matr(matr,i - 1, j) ,
                get_from_matr(matr,i, j - 1)   )
        else:
            matr[i][j] += 1 + min( 
                get_from_matr(matr,i - 1, j - 1) ,
                get_from_matr(matr,i - 1, j) ,
                get_from_matr(matr,i, j - 1)   )


#for i in range(n):
#    print(matr[i])

fout.write( str(matr[n-1][m-1]) )

fout.close()
fin.close()
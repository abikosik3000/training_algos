fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
"""
#triangles = [0] * (n + 1)
prev_flip_triangle = [0] * (n + 1)
flip_triangles = [0] * (n + 1)

for i in range(1,n+1):
    #for size in range(i,0,-1):
    #    triangles[size] += i + 1 - size
    #flip 1
    flip_triangles[1] += i - 1
    for size in range(i // 2 , 1 , -1):
        now_add = prev_flip_triangle[size] + 1
        flip_triangles[size] += now_add
        prev_flip_triangle[size] = now_add

    #print(" ",i)
    #print(triangles)
    #print(flip_triangles)


test_colv = 0
for i in range(1,n+1):
    test_colv += i * (i + 1)
test_colv = test_colv / 2

#print(sum(triangles),test_colv)
"""

#fout.write( str( int(test_colv) + sum(flip_triangles)) )

if(n % 2 == 0 ):
    k = n / 2
    fout.write( str( int(k * ( k + 1)*( 4 *k   + 1)/2)) )
else:
    k = (n - 1) / 2
    fout.write( str( int( (k + 1)*(4* k**2 + 7*k + 2)/2  )) )

fout.close()
fin.close()
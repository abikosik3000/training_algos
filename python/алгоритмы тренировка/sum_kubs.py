fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
import math

n = int(fin.readline().rstrip())


f = [0] * (n+1)
for i in range(1, n+1):
    #f[i] =  f[i-1] + 1
    k = 2
    while k**3 <= i:
        x = f[i-k**3]
        if f[i] > x:
            f[i] = x + 1
        k += 1

print(f)
fout.write( str(f[n]) )


fout.close()
fin.close()

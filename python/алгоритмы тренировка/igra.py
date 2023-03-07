import math
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

buff = fin.readline().rstrip().split(" ") 
n = int(buff[0])
a = int(buff[1])
b = int(buff[2])

'''
dp = [math.inf] *  (n + 1)
minab = min(a,b)
maxab = max(a,b)

dp[0] = 0
dp[1] = 0
dp[2] = maxab
for i in range(2,n+1):
    dp[i+1] = min(dp[i+1],dp[i] + minab)
    dp[i*2] = min(dp[i*2],dp[i] + maxab)
    dp[i*2 + 1] = min(dp[i*2 + 1],dp[i] + maxab)
'''
dp = [0] *  (n + 1)
for i in range(2,n+1):
    variants = []
    for k in range(i-1,0,-1):
        variants.append( max(dp[k] + a , dp[i-k] + b))
    dp[i] = min(variants)

#print(dp)

fout.write( str(dp[n]) )
fout.close()
fin.close()
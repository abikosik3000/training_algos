a = [ int(x) for x in input().rstrip().split(" ") ]
n = a[0]
m = a[1]
k = a[2]

answ = n * k // min(m,n)

print(answ)
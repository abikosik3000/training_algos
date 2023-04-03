import bisect



fin = open('input.txt', 'r')
n = int(fin.readline().rstrip())
a = [ int(x) for x in fin.readline().rstrip().split(" ") ]
fin.close()
'''
n = int(input().rstrip())
a = [ int(x) for x in input().rstrip().split(" ") ]
'''

#print(a)

pref_s_left = [0] * (n + 1)
for i in range(n):
    pref_s_left[i+1] = pref_s_left[i] + a[i]

#print(pref_s_left)

razymes = []
start_buf = dict()
for i in range(n+1):
    if(pref_s_left[i] not in start_buf):
        start_buf.update({pref_s_left[i] : i })
        
    else:
        start = start_buf[pref_s_left[i]]
        razymes.append((start , i -1))
        start_buf.update({pref_s_left[i] : i })

    #print(start_buf)

#for i in range(n):
#    if(a[i] == 0):
#       razymes.append((i , i ))
        
razymes = sorted(razymes ,key= lambda x: x[1])
razymes = sorted(razymes ,key= lambda x: x[0])
#print(razymes)


answ = 0
start_search = 0
for start in range(n):
    norm = start
    start_search = bisect.bisect_left(razymes , start , lo =  start_search ,key= lambda x : x[0])
    #print(start_search)
    min_right = n
    for i in range(start_search ,len(razymes)):
        min_right = min(razymes[i][1] , min_right)
        if(min_right < razymes[i][0]):
            break

    answ += n - min_right

print(answ)
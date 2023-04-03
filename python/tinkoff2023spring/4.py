'''
fin = open('input.txt', 'r')
n = int(fin.readline().rstrip())
a = [ int(x) for x in fin.readline().rstrip().split(" ") ]
fin.close()
'''

n = int(input().rstrip())
a = [ int(x) for x in input().rstrip().split(" ") ]

max_l = 2

d = dict()
max_last_ins = 1
max_ins = 0

max_count = 1
for i in range(n):
    now_int = a[i]
    last_kolv = 0
    if(now_int in d):
        last_kolv = d[now_int]
    d.update({now_int: last_kolv + 1})

    if(max_count == 1):
        max_l = i +1

    if(d[now_int] < max_count - 1):
        continue
    if(d[now_int] == max_count - 1):
        max_last_ins += 1
        #chek
    if(d[now_int] == max_count):
        max_ins += 1
        max_last_ins -= 1
        #chek

    if(d[now_int] > max_count):
        max_last_ins = max_ins - 1
        max_ins = 1
        max_count = d[now_int]
        #chek

    #print(i,a[i] , 'last', max_last_ins , "max" ,max_ins )
    if(max_last_ins + max_ins == len(d) 
       and (max_ins == 1 or max_last_ins == 1)):
        max_l = i +1

print(max_l)
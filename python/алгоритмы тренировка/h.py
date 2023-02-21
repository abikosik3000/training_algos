fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
buf = [ int(x) for x in fin.readline().rstrip().split(" ") ]
n = buf[0]
m = buf[1]
k = buf[2]

matr = [0] * n
for i in range(n):
    matr[i] = [ int(x) for x in fin.readline().rstrip().split(" ") ]

left_sums  = [ [0]*m for _ in range(n)]
top_sums = [ [0]*m for _ in range(n)]

s = 0
for y in range(0,n):
    for x in range(0,m):
        s = s + matr[y][x]
        left_sums[y][x] = s

s = 0
for x in range(0,m):
    for y in range(0,n):
        s = s + matr[y][x]
        top_sums[y][x] = s

#print(top_sums)


def sum_rect_po_left(x1,y1,x2,y2):
    s = 0
    for y in range(y1,y2 + 1):
        s = s + left_sums[y][x2] - left_sums[y][x1] + matr[y][x1]
    return s

def sum_rect_po_top(x1,y1,x2,y2):
    s = 0
    for x in range(x1,x2 + 1):
        s = s + top_sums[y2][x] - top_sums[y1][x] + matr[y1][x]
        #print(top_sums[y2][x] , top_sums[y1][x])
    return s


for i in range(k):
    buf = [ int(x) -1 for x in fin.readline().rstrip().split(" ") ]
    x1 , x2, y1,y2 = buf[1] ,buf[3] ,buf[0] ,buf[2]
    #print(buf)
    s = 0
    if(x2 - x1 > y2 - y1):
        s = sum_rect_po_left(x1,y1,x2,y2)
    else:
        s = sum_rect_po_top(x1,y1,x2,y2)
    fout.write(str(s)+"\n")




fout.close()
fin.close()
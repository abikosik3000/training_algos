fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
a = [ int(x) for x in fin.readline().rstrip().split(" ") ]
prev_num = [None] * n
lenghts = [0] * n

def search_max_val_ind(pos_now):
    max_l = 1
    prev_ind= None
    for i in range(pos_now,-1,-1 ):
        if(a[i] < a[pos_now] and lenghts[i] >= max_l):
            max_l = lenghts[i] + 1
            prev_ind = i

    return (max_l,prev_ind)

for i in range(n):
    max_val_ind = search_max_val_ind(i)
    lenghts[i] = max_val_ind[0]
    prev_num[i] = max_val_ind[1]

#print(a)
#print(prev_num)
#print(lenghts)

now_ind = lenghts.index(max(lenghts))
path = []
while(now_ind != None):
    path.append(str(a[now_ind]))
    now_ind = prev_num[now_ind]


fout.write( " ".join(reversed(path)) )

fout.close()
fin.close()
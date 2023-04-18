
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

buff = [ int(x) for x in fin.readline().rstrip().split(" ") ]
n = buff[0]
m = buff[1]

grass = []
for i in range(n):
    grass.append([ int(x) for x in fin.readline().rstrip() ]) 

'''
buff = [ int(x) for x in input().rstrip().split(" ") ]
n = buff[0]
m = buff[1]

grass = []
for i in range(n):
    grass.append([ int(x) for x in input().rstrip() ]) 
'''

def searc_max(a):
    ret = a[0][0]
    for i in range(n):
        for j in range(m):
            ret = max(ret , a[i][j])
    return ret

def row_and_cort_count_max(a):
    max_a = searc_max(a)
    row_cut = [0] * m
    cort_cut = [0] * n
    for i in range(n):
        for j in range(m):
            if( a[i][j] == max_a):
                cort_cut[i] = cort_cut[i] + 1
                row_cut[j] = row_cut[j] + 1

    return row_cut , cort_cut 
          
def make_cut(grass , row_or_cort , row_cut , cort_cut):
    index = 0
    if(row_or_cort == "cort"):
        index = max(enumerate(cort_cut),key=lambda x: x[1])[0] 
        #print("cort" , index)
        grass[index] = [0] * m
    else:
        index = max(enumerate(row_cut),key=lambda x: x[1])[0] 
        #print("row" , index)
        for i in range(n):
            grass[i][index] = 0
            
    return index


def variabel_cut(_a, cut_1 , cut_2):
    a = list(_a)
    path = [0] * 2
    row_cut , cort_cut = row_and_cort_count_max(a)
    index = make_cut( a,cut_1,row_cut , cort_cut)
    if(cut_1 == "row"):
        path[1] = index + 1
    else:
        path[0] = index + 1

    #print(a)

    row_cut , cort_cut = row_and_cort_count_max(a)
    index = make_cut( a,cut_2,row_cut , cort_cut)
    if(cut_2 == "row"):
        path[1] = index + 1
    else:
        path[0] = index + 1

    #print(a)

    return path , searc_max(a)

v1 = variabel_cut(grass , "row" , "cort")
v2 = variabel_cut(grass , "cort", "row" )
if(v2[1] > v1[1]):
    v1 = v2
print( " ".join( map(str,v1[0] )))
#variabel_cut(grass)




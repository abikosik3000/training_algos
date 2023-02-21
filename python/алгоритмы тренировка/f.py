fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

m = int(fin.readline().rstrip() )
n = int(fin.readline().rstrip() )

razdels = []


def as_intersect(l1 , l2):
    return( l2[0] >= l1[0]  and l2[0] <= l1[1]  or 
            l2[1] >= l1[0]  and l2[1] <= l1[1]  or
            l2[0] < l1[0] and l2[1] > l1[1]
            )


for i in range(n):
    buff = [ int(x) for x in fin.readline().rstrip().split(" ") ]
    now_razdel = (buff[0]  , buff[1])

    new_razdels = []
    for razdel in razdels:
        if(not as_intersect(razdel,now_razdel)):
            new_razdels.append(razdel)

    new_razdels.append(now_razdel)

    razdels = list( new_razdels )

    print(razdels)



fout.write(str(len(razdels)))
fout.close()
fin.close()

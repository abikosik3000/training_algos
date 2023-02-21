fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int( fin.readline().rstrip() )




def get_or_default(l,i , default=None):
    return l[i] if i < len(l) else default


for i in range(n):
    buff = fin.readline().rstrip().split(" ")
    k = int(buff[0])
    konv = [ float(x) for x in buff[1:] ]
    prioritet = list(konv)
    prioritet.sort(reverse=True)

    stek = []
    for i in range(k):
        #print(stek , prioritet)
        now_box = konv[i]
        #print(now_box)

        if(now_box == prioritet[-1]):
            prioritet.pop(-1)
            continue
        
        if(len(stek) == 0):
            stek.append(now_box)
            continue
        
        while(len(stek) > 0):
            if(stek[-1] == prioritet[-1]):
                stek.pop(-1)
                prioritet.pop(-1)
                continue

            break

        stek.append(now_box)


    its_ok =True

    #print("ok")
    #print(stek , prioritet)
    while(len(stek) > 0):
        if(stek[-1] == prioritet[-1]):
            stek.pop(-1)
            prioritet.pop(-1)
            continue

        its_ok = False
        break

    #print(its_ok)
    fout.write(str(int(its_ok)) + "\n")


fout.close()
fin.close()
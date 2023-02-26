import heapq
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

buf = [ int(x) for x in fin.readline().rstrip().split(" ") ]
k = buf[0]
n = buf[1]

depart = dict()
depart_times = []

min_empty = 0
depo = [None] * k
answ = [None] * n

for i in range(n):

    buf = [ int(x) for x in fin.readline().rstrip().split(" ") ]

    #print(depart_times)
    #print(depart)
    while(len(depart_times) > 0):
        if(depart_times[0] >= buf[0]):
            break
        
        depart_list = depart[depart_times[0]]
        for num_depo in depart_list:
            depo[num_depo] = None
            min_empty = min(min_empty , num_depo)
        depart.pop(depart_times[0])
        heapq.heappop(depart_times)

    #error
    if(min_empty == k):
        fout.write("0 "+str(i  +1 ))  
        exit(0)

    #parking
    parking_now = min_empty
    depo[min_empty] = 1
    answ[i] = str(min_empty + 1 )
    while(min_empty < k):
        if(depo[min_empty] is None):
            break
        min_empty += 1

    # add depart
    depart_temp = []
    if(buf[1] in depart):
        depart_temp = depart[buf[1]]
    else:
        heapq.heappush(depart_times, buf[1])
    depart_temp.append(parking_now)    
    depart.update({ buf[1] : depart_temp })



fout.write("\n".join(answ ))

fout.close()
fin.close()
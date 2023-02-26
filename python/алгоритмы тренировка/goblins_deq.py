from collections import deque

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
deq = deque(maxlen=n + 1)#maxlen=n*2
count_deq = 0

for i in range(n):
    comand = fin.readline().rstrip().split(" ")
    if(comand[0] == "-"):
        fout.write( deq[0].popleft() +"\n" )
        if(len(deq[0]) == 0):
            deq.popleft()
        count_deq -= 1

    elif(comand[0] == "*"):
        ind = len(deq) // 2 + len(deq) % 2
        deq.insert(ind, comand[1])
        count_deq += 1
    #print(deq)
    print(deq[-1])



#fout.write( "\n".join(map(str,answ)) )

fout.close()
fin.close()
#fin = open('input.txt', 'r')
#fout = open('output.txt', 'w')

#n = int(fin.readline().rstrip())
#contr = [ int(x) for x in fin.readline().rstrip().split(" ") ]

n = int(input().rstrip())
contr = [ int(x) for x in input().rstrip().split(" ") ]

max_i = 0
min_i = 0
for i in range(n):
    if(contr[i] >= contr[max_i]):
        max_i = i

    if(contr[i] < contr[min_i]):
        min_i = i

print( str(max_i + 1)+" "+str(min_i + 1) )
#fout.write( "".join(map(str,answ)) )
#fout.close()
#fin.close()
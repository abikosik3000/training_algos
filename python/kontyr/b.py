#fin = open('input.txt', 'r')
#fout = open('output.txt', 'w')

n = int(input().rstrip())
nails_set = set()

'''
for i in range(n):
   nails_set.add(tuple(( int(x) for x in fin.readline().rstrip().split(" ") )))
'''
for i in range(n):
   nails_set.add(tuple(( int(x) for x in input().rstrip().split(" ") )))


def S(n1,n2):
    return abs(n1[0] - n2[0]) * abs(n1[1] - n2[1])

max_s = 0
for nail in nails_set:
    for nail2 in nails_set:

        if(nail2 == nail):
            continue

        if((nail[0] , nail2[1] ) in nails_set 
           and (nail2[0] , nail[1] ) in nails_set):
            max_s = max(max_s ,S(nail,nail2) )

print(str(max_s))
#print( str(max_i + 1)+" "+str(min_i + 1) )
#fout.write( "".join(map(str,answ)) )
#fout.close()
#fin.close()
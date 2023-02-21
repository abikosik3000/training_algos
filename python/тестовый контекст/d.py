fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')


s1 = fin.readline().rstrip()
s2 = fin.readline().rstrip()
set_1 = {}

for s in s1:
    now_count = 1
    if(s in set_1):
        now_count = set_1[s] + 1
    set_1.update( {s:now_count} )


is_anagramm = True
for s in s2:

    if(s not in set_1):
        is_anagramm = False
        break
    
    now_count = set_1[s] - 1
    if(now_count > 0 ):
        set_1.update({s : now_count})

    if(now_count == 0):
        set_1.pop(s)


fout.write(str(int(is_anagramm)))
fin.close()
fout.close()
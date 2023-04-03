fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

def str_to_num(s):
    if(s == "N"):
        return 0
    elif(s == "S"):
        return 1
    elif(s == "W"):
        return 2
    elif(s == "E"):
        return 3
    elif(s == "U"):
        return 4
    elif(s == "D"):
        return 5
    
def multi_vector(v , x):
    ret = list(v)
    for i in range(len(ret)):
        ret[i] = ret[i] * x

    return ret

def add_to_vector(v1,v2):
    for i in range(len(v2)):
        v1[i] += v2[i]
    
programs = [0] * 6
for i in range(6):
    buff = list( map( str_to_num , fin.readline().rstrip() ) )
    programs[i] = [ buff.count(x) for x in range(6)]

buff = fin.readline().rstrip().split(" ") 
strt_call = str_to_num(buff[0])
k = int(buff[1])

calls = [ [0] * 6 for i in range(k) ] 
calls[0][strt_call] = 1

for i in range(1,k):
    for j in range(6): 
        add_to_vector(calls[i], multi_vector( programs[j],calls[i - 1][j]))
    
answ = 0
for x in calls:
    answ = answ + sum(x) 
#print(answ)
fout.write( str( answ ))


fout.close()
fin.close()
import math
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

slovo = fin.readline().rstrip()

dict_answ = {}
for i in range(97,123):
    dict_answ.update( {chr(i) : 0 })  

n = len(slovo)

def min_otstyp(i):
    return min(i + 1 ,n - i)

last_p = None
now_p = None

for i in range( math.floor(n / 2) + (n % 2) ):
    if(last_p == None):
        now_p = n
    else:
        now_p = last_p + (n - min_otstyp(i - 1) * 2)

    dict_answ[slovo[i]] += now_p
    if(i != n - i - 1):
        dict_answ[slovo[n - 1 - i]] += now_p
    last_p = now_p

for k,v in dict_answ.items():
    if(v == 0):
        continue
    fout.write(k +": "+str(v)+"\n")

fout.close()
fin.close()
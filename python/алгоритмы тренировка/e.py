fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip() )

nabor = []

for i in range(n):
    nabor.append(int(fin.readline().rstrip() ))

godless = 0

for len_commbo in range(n,1,-1):
    for start_combo in range(0,n - len_commbo + 1):
        srez = slice(start_combo,start_combo + len_commbo)
        minimum = min(nabor[srez])
        if(minimum > 0 ):
            godless += (len_commbo - 1) * minimum
            nabor[srez] = map( lambda x : x - minimum , nabor[srez])
    

fout.write(str( godless) )


fout.close()
fin.close()

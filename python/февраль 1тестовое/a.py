fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')


n = int(fin.readline())
simvols = fin.readline().rstrip().split(" ") 
rows = fin.readline().rstrip().split(" ")

k = int(fin.readline())
referat =  fin.readline().rstrip().split(" ")


simv_row = {}
for k,v in zip(simvols , rows):
    simv_row.update({k:v})


last_row = None
razriadnost = 0
for x in referat:
    now_row = simv_row[x]
    if(last_row != None and now_row != last_row):
        razriadnost = razriadnost + 1
    last_row = now_row

#print(simv_row)

fout.write(str(razriadnost))
fin.close()
fout.close()
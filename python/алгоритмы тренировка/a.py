fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')
lines = fin.readlines()

dict_symbol = {}

for line in lines:
    for symbol in line.rstrip():
        
        if symbol == " ":
            continue

        now_count = dict_symbol.get(symbol,0) + 1

        dict_symbol.update({symbol : now_count})

sorted_dict = dict_symbol.items()
sorted_dict = sorted(sorted_dict , key=lambda x : x[0] )
dict_symbol = dict(sorted_dict)
max_in = max(dict_symbol.values())



#print(max_in)
for now_in in range(max_in , 0 , -1):
    strng_out = ""
    for ins in dict_symbol.values():
        strng_out = strng_out + ('#' if ins >= now_in else ' ')
        
    fout.write(strng_out+'\n')

fout.write(''.join(dict_symbol.keys()))

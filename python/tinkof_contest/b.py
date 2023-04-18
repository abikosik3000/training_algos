fin = open('input.txt', 'r')

s = fin.readline().rstrip()


st = {1026, 1027, 1029, 1030, 1033, 1034, 1035, 1036, 1039, 1169,
       8470, 8216, 8218, 8222, 1056, 1057, 8224, 8225, 8230, 8364, 
       8240, 176, 177, 181, 182, 183, 8249, 187, 67, 1105, 1107, 
       1108, 1109, 1110, 1111, 1112}

chek_s = set()

for i in range(len(s)):
    if(ord(s[i].lower()) in st):
        print(s[i].lower())
        chek_s.add( s[i].lower())

print(len(chek_s))
print(len(chek_s) == 33)



#buff = [ int(x) for x in fin.readline().rstrip().split(" ") ]


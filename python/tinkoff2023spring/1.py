#fin = open('input.txt', 'r')
#fout = open('output.txt', 'w')

a = [ int(x) for x in input().rstrip().split(" ") ]

upper = None
answ = "YES"

for i in range(1,len(a)):
    if(a[i] == a[ i - 1]):
        continue
    if(upper is None):
        upper = a[i - 1] < a[i]
        continue
    if (upper != (a[i - 1] < a[i])):
        answ = "NO"
        break

print(answ)
#fout.write(answ)

#fout.close()
#fin.close()
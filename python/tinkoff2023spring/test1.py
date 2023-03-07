fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
m = int(fin.readline().rstrip())


fout.write( str(n + m) )

fout.close()
fin.close()

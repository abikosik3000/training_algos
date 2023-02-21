fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')


n = int(fin.readline().rstrip())

l = n * 2


def rec(s , otkr, zakr):
    if(otkr == 0 and zakr == 0):
        fout.write(s+"\n")

    if(otkr > 0):
        rec(s + "(" , otkr - 1, zakr + 1)

    if(zakr > 0):
        rec(s + ")" , otkr , zakr - 1)

rec('',n ,0)

fin.close()
fout.close()
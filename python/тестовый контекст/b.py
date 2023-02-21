fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

n = int(fin.readline().rstrip())
biggest_combo = 0
now_combo = 0
for i in range(n):

    now_num = int(fin.readline().rstrip())
    if(now_num == 1):
        now_combo = now_combo + 1
    if(now_num == 0):
        biggest_combo = max(biggest_combo , now_combo)
        now_combo = 0

biggest_combo = max(biggest_combo , now_combo)


fout.write(str(biggest_combo))

fin.close()
fout.close()
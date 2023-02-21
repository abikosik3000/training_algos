from datetime import datetime , timedelta , time , timezone
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

def rd(x,y=0):
    m = int('1'+'0'*y)
    q = x*m
    c = int(q)
    i = int( (q-c)*10 )
    if i >= 5:
        c += 1
    return c/m

a = fin.readline().rstrip() 
b = fin.readline().rstrip() 
c = fin.readline().rstrip() 

format = "%H:%M:%S"
a = datetime.strptime(a , format)
b = datetime.strptime(b , format)
c = datetime.strptime(c , format)

if(c < a):
    c = c + timedelta(days=1)

timestamp_a = a.replace(tzinfo=timezone.utc).timestamp()
timestamp_c = c.replace(tzinfo=timezone.utc).timestamp()
delta = rd( abs(timestamp_a - timestamp_c ) / 2  )


hours = delta // 3600
delta = delta - hours * 3600
minutes = delta // 60
delta = delta - minutes * 60
sec = delta

now_time = b + timedelta(hours=hours , minutes=minutes, seconds=sec)

fout.write( datetime.strftime(now_time , format))

fout.close()
fin.close()

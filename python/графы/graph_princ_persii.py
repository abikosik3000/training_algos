#один конь Z Y X
import math

def all_variants(coords , lab):
    vars = []
    dist = []
    h,m,n = len(lab) , len(lab[0]) , len(lab[0][0]) 
    
    for add in [ ( 0 , 1 , 0) , ( 0 , -1 , 0) , ( 0 , 0 , 1) , ( 0 , 0 , -1) , ( 1 , 0 ,0)]:
        buf = (coords[0] + add[0], coords[1] + add[1], coords[2] + add[2])
        if(buf[1] >= 0 and buf[2] >= 0
         and buf[1] < m and buf[2] < n 
         and buf[0] < h):
            
            if(lab[buf[0]][buf[1]][buf[2]] != 'o'):
                vars.append( buf )
                dist.append( 5 )

    return vars , dist

def bfs(a ,z1,y1,x1):
    visited = set()
    distanses = {}
    distanses.update({(z1,y1,x1) : 0 })

    stack = []
    stack.append((z1 , y1 , x1))

    while(len(stack) > 0):
        now_coord = stack.pop(0)

        if(now_coord in visited):
            continue
        visited.add(now_coord)

        #print(now_coord)
        
        shag_variants  , shag_dist = all_variants(now_coord , a)
        for next_coord , next_dist in zip( shag_variants , shag_dist):
            
            last_dist_to_next = math.inf
            if(next_coord in distanses):
                last_dist_to_next = distanses[next_coord]

            dist_to_next = distanses[now_coord] + next_dist
            if( dist_to_next < last_dist_to_next):
                distanses.update({next_coord : dist_to_next})
                stack.append(next_coord)

    return distanses



fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

buf = [int(num) for num in fin.readline().split(" ")] 
h = buf[0]
m = buf[1]
n = buf[2]

lab = [[[0 for k in range(n)] for j in range(m)] for i in range(h)]


start = ()
final = ()

for i_h in range(h):
    for i_m in range(m):
        s = fin.readline()
        for i_n in range(n):
            buf = s[i_n]

            if(s[i_n] == '1'):
                start = (i_h , i_m , i_n )
                buf = '.'

            if(s[i_n] == '2'):
                final = (i_h , i_m , i_n )
                buf = '.'

            if(buf == "."):
                buf = 0

            lab[i_h ][ i_m ][ i_n ] = buf
    fin.readline()

print(lab)
#print(start)
print(final)

distantions = bfs(lab , start[0], start[1], start[2] )

fout.write(str( distantions[final[0], final[1] , final[2]] ) )

fin.close()
fout.close()
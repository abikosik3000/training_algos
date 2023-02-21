#один конь
import math

def all_variants(coords , n):
    vars = []
    for x in ( 2 , -2):
        for y in ( 1 , -1):
            buf = (coords[0] + x , coords[1] + y)
            if(buf[0] > 0 and buf[1] > 0 and buf[0] <= n and buf[1] <= n):
                vars.append( buf )

    for x in ( 1 , -1):
        for y in ( 2 , -2):
            buf = (coords[0] + x , coords[1] + y)
            if(buf[0] > 0 and buf[1] > 0 and buf[0] <= n and buf[1] <= n):
                vars.append( buf )

    return vars

def bfs(x1,y1,x2,y2,n):
    visited = set()
    distanses = {}
    distanses.update({(x1,y1) : 0 })

    stack = []
    stack.append((x1 , y1))

    while(len(stack) > 0):
        now_coord = stack.pop(0)

        if(now_coord in visited):
            continue
        visited.add(now_coord)

        #print(now_coord)
        
        variants = all_variants(now_coord , n)
        for next_coord in variants:
            
            last_dist_to_next = math.inf
            if(next_coord in distanses):
                last_dist_to_next = distanses[next_coord]

            dist_to_next = distanses[now_coord] + 1
            if( dist_to_next < last_dist_to_next):
                distanses.update({next_coord : dist_to_next})
                stack.append(next_coord)

    return distanses



fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

n = int( fin.readline() )

buf = [int(num) for num in fin.readline().split(" ")] 
x1 = buf[0]
y1 = buf[1]

buf = [int(num) for num in fin.readline().split(" ")] 
x2 = buf[0] 
y2 = buf[1]

rez = bfs(x1,y1 , x2,y2,n)
fout.write(str( rez[(x2,y2)] ) )

fin.close()
fout.close()
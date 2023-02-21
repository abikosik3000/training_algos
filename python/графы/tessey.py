import math

def next_step(dis , visited  , coords ):
    vars = []
    dist = []
    global g

    print(coords)

    if(not( coords == (0 , 0))):
            
        
        for add in [ (0 , 1) , (1 , 0) , ( 0 , -1) , ( -1 , 0) ]:
            buf = (coords[0] + add[0], coords[1] + add[1])
            if( buf in dis and not(buf in visited)):
                if(buf in g.search_node(coords).edges ):
                    vars.append( buf )
                    dist.append( dis[buf])
                    visited.add(buf)

        min_dist = min(dist)

        i = 0
        next = vars[i]
        while(dis[next] != min_dist):
            i += 1
            next = vars[i]

        diff = (next[0] - coords[0] , next[1] - coords[1] )
        global answ
        global bokvi
        answ = answ + bokvi[diff]

        if(not( next == (0 , 0))):
            next_step(dis , visited  , next )

class Node:

    def __init__(self , name , edges = [] , long_edges = None):
        self.name = name
        self.edges = set(edges)
        if(long_edges is None):
            long_edges = [ 1 ] * len(edges)
        self.long_edges = dict( zip(edges , long_edges) )
              
    def __repr__(self) -> str:
        s = str(self.name) + " - "
        for x in self.edges:
            s = s + str(x)
        return s

    def update_edges(self,edges , long_edges = None):

        if(long_edges is None):
            long_edges = [ 1 ] * len(edges)

        for edg , long in zip(edges , long_edges):
            self.edges.add(edg)
            self.long_edges.update({edg : long})



    def dist_to(self , name):
        return self.long_edges[name]

class Graph:

    def __init__(self):
        self.nodes = {}
      
    def add_node(self,name, edges = []):
        self.nodes.update( { name : Node(name , edges)} )

    def update_node(self,name, edges = []):
        node = self.search_node(name)
        if(node is None):
            self.add_node(name, edges)
        else:
            node.update_edges(edges)

    def __repr__(self) -> str:
        s = ""
        for x in self.nodes.values():
            s = s + str(x) + "\n"
        return s
        
    def search_node(self, name):
        #search Node or None
        if(name in self.nodes):
            return self.nodes[name]

        return None #TODO raise

    def dfs(self , start_node_name , fin_node_name ,callback = print):
        visited = set()
        path = []

        def __dfs(node_name):

            if(node_name in visited):
                return False
            
            node = self.search_node(node_name)
            visited.add(node_name)
            #callback(node)

            #конец обхода
            search_end = ( node_name == fin_node_name )

            for next_node in node.edges:
                if(search_end): 
                    break
                search_end = __dfs(next_node)

            if(search_end):
                path.append(node.name)
            return search_end

        search_end = __dfs(start_node_name)
        return{ "search_end" : search_end , "path" : path }

        
    def restore_path(self , node_name , relaks_from):
        path = []
        path.insert(0 ,node_name)

        while(node_name in relaks_from):
            node_name = relaks_from[node_name]
            path.insert(0 ,node_name)

        return path

    def bfs(self , start_node_name , fin_node_name ,callback = print):
        
        search_end = False
        distantion = { x : math.inf for x in self.nodes.keys()}
        relaks_from = {}
        #path = []

        node = self.search_node(start_node_name)
        distantion.update({node.name : 0})
        
        q = []
        q.append(node)

        while(len(q) > 0):
            node = q.pop(0)
            #callback(node)

            if(node.name == fin_node_name):
                search_end = True

            for next_node_name in node.edges:
                next_node = self.search_node(next_node_name)

                dist_to_next = distantion[node.name] + node.dist_to(next_node.name)
                if( dist_to_next <  distantion[next_node.name] ):
                    distantion.update({next_node.name : dist_to_next})
                    relaks_from.update({next_node.name : node.name})
                    q.append(next_node)
                
        path = self.restore_path(fin_node_name, relaks_from)        
        return{ "search_end" : search_end , "relaks_from" : relaks_from , "distantion" : distantion  , "path" : path}


fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

g = Graph()

s = fin.readline().strip()

class Cord:
    def __init__(self , typle):
        self.x = typle[0]
        self.y = typle[1]

    def move(self , typle):
        self.x += typle[0]
        self.y += typle[1]
    
    @property
    def to_typle(self):
        return (self.x , self.y)





moves = {"N" : ( 0 , 1),"S" : ( 0 , -1),"W" : ( -1 , 0), "E" : ( 1 , 0)}
bokvi = { (0, 1) : "N", ( 0 , -1): "S" ,( -1 , 0) :  "W" ,  ( 1 , 0) : "E" }
now = Cord( (0 , 0) )
g.add_node(now.to_typle , [])

for x in s:
    next = Cord(now.to_typle)
    next.move(moves[x])
    g.update_node(next.to_typle , [now.to_typle])
    g.update_node(now.to_typle , [next.to_typle])
    now = Cord(next.to_typle)


print(g)


rez = g.bfs((0,0) , (0,0))   

dis = rez['distantion']
visited = set()
visited.add( now.to_typle )

answ = ""
print(dis)

next_step(dis , visited  , now.to_typle  )


fout.write(answ.strip())


fin.close()
fout.close()
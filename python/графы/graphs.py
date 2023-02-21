import math

class Node:

    def __init__(self , name , edges = [] , long_edges = None):
        self.name = name
        self.edges = edges
        if(long_edges is None):
            long_edges = [ 1 ] * len(edges)
        self.long_edges = dict( zip(edges , long_edges) )
              
    def __repr__(self) -> str:
        s = str(self.name) + " - "
        for x in self.edges:
            s = s + str(x)
        return s

    def dist_to(self , name):
        return self.long_edges[name]

class Graph:

    def __init__(self):
        self.nodes = {}
      
    def add_node(self,name, edges = []):
        self.nodes.update( { name : Node(name , edges)} )

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

buf = [int(num) for num in fin.readline().split(" ")] 
n = buf[0]
s = buf[1]

def complete_to_graph(arr):
    ret = []
    for i in range(len(arr)):
        if(arr[i] != 0 ):
            ret.append(i)
    return ret


g = Graph()
for i in range(n):
    buff = [int(num) for num in fin.readline().split(" ")]  
    g.add_node(i, complete_to_graph(buff))

#print(g)

rez = g.bfs(s,s)
#print(rez)
answer = len( 
    list( 
        filter( 
            lambda x : x != math.inf , 
            rez['distantion'].values() 
            ) 
    ) 
    ) - 1

fout.write(str( answer) )

fin.close()
fout.close()

'''
g = Graph()
g.add_node(0 , [1 , 2 , 8])
g.add_node(1 , [9 , 0])
g.add_node(2 , [4 , 0])
g.add_node(3 , [5 , 9])
g.add_node(4 , [5 , 6 , 2])
g.add_node(5 , [4 , 3])
g.add_node(6 , [7 , 4])
g.add_node(7 , [6 , 8])
g.add_node(8 , [7 , 0 , 6])
g.add_node(9 , [3 , 1])
rez = g.bfs(0,7)
print(rez["relaks_from"])
print( g.restore_path( 7, rez["relaks_from"]) )
'''
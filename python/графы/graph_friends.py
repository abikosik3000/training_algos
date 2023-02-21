#друзья
class Graph_arr:

    def __init__(self):
        self.nodes = []

    def add_node(self, node_joins):
        self.nodes.append(node_joins)

    def joins(self, node):
        return self.nodes[node]

    def __repr__(self):
        s = ""
        for i,x in enumerate( self.nodes):
            s = s + str(i) + " " + str(x) + "\n"
        return s

    def dfs(self , start_node):
        stack = []
        visited = set()
        count = -1
        stack.append(start_node)

        while(len(stack) > 0):
            node = stack.pop(-1)

            if(node in visited):
                continue
            visited.add(node)
            count += 1
            #print(node)
            joins = self.joins(node)
            for i in range(len(joins)):
                if joins[i] != 0:
                    stack.append(i)

        return count

fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

buf = [int(num) for num in fin.readline().split(" ")] 
n = buf[0]
s = buf[1] - 1

g = Graph_arr()
for i in range(n):
    g.add_node( [int(num) for num in fin.readline().split(" ")] )

print(g)

fout.write( str( g.dfs(s) ))

fin.close()
fout.close()
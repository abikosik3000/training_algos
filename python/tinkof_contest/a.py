fin = open('input.txt', 'r')

class Node:
    def __init__(self ,data = None ):
        self.nods = []
        self.data = data

s = fin.readline().rstrip()
a = [0] * len(s)
for i in range(len(s)):
    a[i] = s[i]

a = sorted(a)

tree = Node(str(a[0]))

def persitions(tree,a,i):
    if(i == len(a)):
        return 0
    
    for j in range(i,len(a)):
        buff = tree.data
        buff = buff + str(a[j])
        new_node = Node(buff)
        tree.nods.append(new_node)
        persitions(new_node, a ,i +1)
    

persitions(tree,a,1)

answ = []
def foo(tree):
    answ.append(tree.data)
    for i in range(len(tree.nods)):
        foo(tree.nods[i])
foo(tree)
print(answ)
#buff = [ int(x) for x in fin.readline().rstrip().split(" ") ]


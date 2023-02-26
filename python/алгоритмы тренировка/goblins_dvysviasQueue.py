
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        s = "("
        if(self.prev is  None):
            s += "none"
        else:
            s += str(self.prev.data)

        s += " "+str(self.data)+" "
        if(self.next is  None):
            s += "none"
        else:
            s += str(self.next.data)
        return s + ")"
          
class Queue:
  
    def __init__(self):
        self.head = None
        self.last = None
        self.middle = None
        self.size = 0
          
    def add(self, data):
        self.size = self.size + 1
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
            self.middle = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev= self.last
            self.last = self.last.next
            if(self.size % 2 == 1):
                self.middle = self.middle.next

    def insert_midle(self, data):
        self.size = self.size + 1
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
            self.middle = self.head
        else:
            temp_next = self.middle.next
            self.middle.next = Node(data)
            self.middle.next.prev = self.middle
            self.middle.next.next = temp_next
            if(not(temp_next is None)):
                temp_next.prev = self.middle.next 
                
            if(self.size == 2):
                self.last = self.middle.next
            if(self.size % 2 == 1):
                self.middle = self.middle.next
            
              
    def pop(self):
        self.size = self.size - 1
        if self.head is None:
            return None
        elif(self.head.next is None):
            temp= self.head.data
            self.head = None
            self.last = None
            self.middle = None
            return temp
        else:
            temp= self.head.data
            self.head = self.head.next
            self.head.prev = None
            if(self.size % 2 == 1):
                self.middle = self.middle.next
            return temp
  
    def first(self):
        return self.head.data
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
              
    def printqueue(self):
        temp=self.head
        while temp is not None:
            print(temp,end="->")
            temp=temp.next
        if not(self.middle is None):
            print("\n midle", self.middle)


      
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
q = Queue()
count_deq = 0

for i in range(n):
    comand = fin.readline().rstrip().split(" ")
    if(comand[0] == "-"):
        fout.write( q.pop() +"\n" )
    elif(comand[0] == "+"):
        q.add(comand[1])
    elif(comand[0] == "*"):
        q.insert_midle(comand[1])

    #q.printqueue()

fout.close()
fin.close()
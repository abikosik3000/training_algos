class Deck:

    def add_front(self , x):
        self.count += 1
        self.front = (self.front - 1) % self.n
        self._arr[self.front] = x

    def pop_front(self):
        self.count -= 1
        ret = self._arr[self.front]
        self._arr[self.front] = None
        self.front = (self.front + 1) % self.n
        return ret

    def peek_front(self):
        return self._arr[self.front]

    def add_back(self , x):
        self.count += 1
        self.back = (self.back + 1) % self.n
        self._arr[self.back] = x

    def pop_back(self):
        self.count -= 1
        ret = self._arr[self.back]
        self._arr[self.back] = None
        self.back = (self.back - 1) % self.n
        return ret

    def peek_back(self):
        return self._arr[self.back]

    def __init__(self , n):
        self.n = n
        self._arr = [None] * n
        self.front = 0
        self.back = -1 % n
        self.count = 0

    def __repr__(self):
        i = self.front
        #print("f b",self.front , self.back , self._arr)
        s = "\n"+ str(self._arr[i])
        while (i != self.back):
            i = (i + 1) % self.n
            s = s + " " + str(self._arr[i])
        return s


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

buff = fin.readline().rstrip().split(" ") 
n = int(buff[0])
k = int(buff[1])
a = [ int(x) for x in fin.readline().rstrip().split(" ") ]

answ = []
deck = Deck(n )#+ 10

for x in a[0:k]:
    # print(deck)
    if(deck.count == 0):
        deck.add_back(x)
        continue

    while(deck.count > 0):
        if(deck.peek_back() <= x):
            break
        deck.pop_back()

    deck.add_back(x)

answ.append(deck.peek_front())

for i in range(k,n):
    
    if(deck.count > 0):
        if(deck.peek_front() == a[i - k]):
            deck.pop_front()

    while(deck.count > 0):
        if(deck.peek_back() <= a[i]):
            break
        deck.pop_back()

    deck.add_back(a[i])
    answ.append(deck.peek_front())


fout.write( "\n".join(map(str,answ)) )

fout.close()
fin.close()
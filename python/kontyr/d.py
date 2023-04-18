'''
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline().rstrip())
dices = [0] * n
for i in range(n):
    dices[i] = sorted([ int(x) for x in fin.readline().rstrip().split(" ") ])
    
'''
n = int(input().rstrip())
dices = [0] * n
for i in range(n):
    dices[i] = [ int(x) for x in input().rstrip().split(" ") ]
    
#
number = [0] * n
def add_one(number):
    number[0] = number[0] + 1
    for i in range(n - 1):
        if(number[i] == 6):
            number[i] = 0
            number[i + 1] = number[i + 1]  + 1

kombinations = set()

for i in range(pow(6 ,n )):
    
    num = 0
    for i in range(n):
        num = num + dices[i][number[i]]
    kombinations.add(num)
    add_one(number)


print(len(kombinations))
'''
print(dices)

kombinations = set()
heap = []
sum_grain = 0
for i in range(n):
    heapq.heappush(heap, ( dices[i][0] , i ,0))
    sum_grain = sum_grain + dices[i][0]

last_grain = [0] * n
kombinations.add(sum_grain)
while(len(heap) > 0):

    x = heapq.heappop(heap)
    sum_grain = sum_grain - x[0]
    if(x[2] == 5):
        last_grain[x[1]] = x[0]
    else:
        heapq.heappush(heap, ( dices[x[1]][x[2] + 1 ] , x[1] ,x[2] + 1))
        sum_grain = sum_grain + dices[x[1]][x[2] + 1 ] 

    kombinations.add(int(sum_grain) + int(sum(last_grain)))

print(kombinations)
print(len(kombinations))
'''
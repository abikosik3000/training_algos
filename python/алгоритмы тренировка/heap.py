import heapq
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n =  int(fin.readline().rstrip())

heap = [ int(x) for x in fin.readline().rstrip().split(" ") ]
cost = 0

heapq.heapify(heap)

while(len(heap) > 1):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    sum = x + y
    heapq.heappush(heap ,sum)
    cost += sum / 100 * 5

fout.write(str('%.2f' % cost))

fout.close()
fin.close()
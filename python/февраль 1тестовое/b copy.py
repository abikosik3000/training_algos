fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


buf = [int(num) for num in fin.readline().rstrip().split(" ")] 
n = buf[0]
x = buf[1]
t = buf[2]

skylpts = [int(num) for num in fin.readline().rstrip().split(" ")] 

skylpts_t = [abs(num - x) for num in skylpts] 

sort_skylpts_t = skylpts_t.copy()
quick_sort(sort_skylpts_t)

#print(skylpts)
#print(skylpts_t)
#print(sort_skylpts_t)

colv = 0
max_t_in = -1
for i in range(n):
    need_t = sort_skylpts_t[i]

    if(t - need_t < 0):
        break

    t = t - need_t
    colv = colv + 1
    max_t_in = need_t

answ = []
for i in range(n):
    if(skylpts_t[i] < max_t_in):
        answ.append(str(i + 1))
        colv = colv - 1

for i in range(n):

    if(colv == 0):
        break

    if(skylpts_t[i] == max_t_in):
        answ.append(str(i + 1))
        colv = colv - 1

fout.write(str(len(answ))+'\n')
fout.write(" ".join(answ))

fin.close()
fout.close()
'''
need_t = {}
for skylpt in skylpts:
    now_need_t = abs(skylpt - x)
    count_t = 1
    if(now_need_t in need_t):
        count_t = count_t + need_t[now_need_t]
    need_t.update({now_need_t : count_t})
'''

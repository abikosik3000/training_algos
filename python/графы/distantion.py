import math
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


import math
from functools import lru_cache
fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

buf = [int(num) for num in fin.readline().split(" ")] 
n = buf[0]
k = buf[1]

ishod_a = [int(num) for num in fin.readline().split(" ")] 

sort_a = ishod_a.copy()
quick_sort(sort_a)
#sort_a = sorted(sort_a)

left_a = []
right_a = []
left_a.append(math.inf)
for i in range(1,n):
    left_a.append(sort_a[i] - sort_a[i - 1])
    right_a.append(sort_a[i] - sort_a[i - 1])

right_a.append(math.inf)

#print(sort_a , left_a ,right_a )

@lru_cache(maxsize=None)
def min_s(start_index):
    now_sum = 0
    left_i = start_index
    right_i = start_index
    left = left_a[left_i]
    right = right_a[right_i]
    for i in range(k):
        if(left < right):
            now_sum = now_sum + left
            left_i = left_i - 1
            left = left +  left_a[left_i]
        else:
            now_sum = now_sum + right
            right_i = right_i + 1
            right = right +  right_a[right_i]
    
    return str(now_sum)


answ  = []
for x in ishod_a:
    start_index = sort_a.index(x)

    buf = min_s(start_index)
    answ.append(buf)

fout.write(" ".join( answ ))


fin.close()
fout.close()
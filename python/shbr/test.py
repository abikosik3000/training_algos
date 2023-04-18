from sortedcontainers import SortedList
import random
import time
import sys
import heapq
 
class MaxHeap:
 
    # Инициализировать максимальную кучу
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
 
    # Поместить элемент в максимальную кучу, сохраняя инвариантность кучи
    def push(self, item):
        heapq.heappush(self.data, -item)
 
    # Вытолкнуть самый большой элемент из максимальной кучи, сохраняя инвариантность кучи
    def pop(self):
        return -heapq.heappop(self.data)
 
    # Извлекать и возвращать текущее наибольшее значение, а также добавлять новый элемент
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)
 
    # Возвращает текущее наибольшее значение в максимальной куче
    def top(self):
        return -self.data[0]

random.seed(12345678)
numbers = SortedList()
h = []
'''
numbers.add(2)
numbers.add(2)
print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])

'''

# adding 10 ** 6 random elements - 999936 unique
last_time = time.time()
for _ in range(10 ** 6):
    #numbers.add(random.randint(1, 10 ** 10))
    heapq.heappush(h,random.randint(1, 10 ** 10))
print("Addition time:", round(time.time() - last_time, 3))
print(sys.getsizeof(h) / 1024 / 1024)
'''
# checking is element in set for 10 ** 6 random numbers
last_time = time.time()
for _ in range(10 ** 6):
    #is_element_in_set = random.randint(1, 10 ** 10) in numbers
print("Checking time:", round(time.time() - last_time, 3))


# getting index for all elements
last_time = time.time()
requests = list(numbers)
random.shuffle(requests)
for elem in requests:
    answer = numbers.index(elem)
print("Getting indexes time:", round(time.time() - last_time, 3))

# getting elements by indexes 10 ** 6 times
requests = list(numbers)
random.shuffle(requests)
last_time = time.time()
for _ in range(10 ** 6):
    answer = numbers[0]
print("Getting elements time:", round(time.time() - last_time, 3))

# deleting all elements one by one
random.shuffle(requests)
last_time = time.time()
for elem in requests:
    numbers.discard(elem)
print("Deleting time:", round(time.time() - last_time, 3))
'''

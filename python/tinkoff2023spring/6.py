'''
'''
def partition(nums, low, high , key):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i][key] < pivot[key]:
            i += 1

        j -= 1
        while nums[j][key] > pivot[key]:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums,key ):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high,key)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

fin = open('input.txt', 'r')
buf = [ int(x) for x in fin.readline().rstrip().split(" ") ]
n = buf[0]
s = buf[1]
students = [0] * n
for i  in range(n):
    students[i] = tuple( int(x) for x in fin.readline().rstrip().split(" ") )
    print(students[i] )

students = sorted(students,key= lambda x: x[1])
students = sorted(students,key= lambda x: x[0])

print(students)

answ = 0
perestanovka = 0
left = n//2
for i in range(n//2, n):
    if(i != n//2):
        pass    
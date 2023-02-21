import math

def partition(nums, low, high ):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    #MNOGO = 10000000000
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while (nums[i]["dohod"]  ) < ( pivot["dohod"]  ):
            i += 1

        j -= 1
        while  (nums[j]["dohod"]  ) > ( pivot["dohod"]  ):
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums ):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

n = int( fin.readline().rstrip() )
c_dohod = [int(num) for num in fin.readline().rstrip().split(" ")] 
c_obr = [int(num) for num in fin.readline().rstrip().split(" ")] 
c_parent = [int(num) for num in fin.readline().rstrip().split(" ")] 

q = int( fin.readline().rstrip() )
s_dohod = [int(num) for num in fin.readline().rstrip().split(" ")] 
s_obr = [int(num) for num in fin.readline().rstrip().split(" ")] 
s_parent = [int(num) for num in fin.readline().rstrip().split(" ")] 

countries = []
countries_no_obr = []
can_parent_countru_nums = set()
for i in range(n):
    buf = { 'id' : i  +1 , 'dohod' : c_dohod[i] ,'obr' : c_obr[i] ,'parent' : c_parent[i]  }
    countries.append( buf )
    if(c_obr[i] == 0):
        countries_no_obr.append( buf )
    if(c_parent[i] == 1):
        can_parent_countru_nums.add(i + 1)

students_obr = []
students_no_obr = []
for i in range(q):
    buf = { 'id' : i + 1 , 'dohod' : s_dohod[i] ,'obr' : s_obr[i] ,'parent' : s_parent[i]  }
    if(s_obr[i] == 0):
        students_no_obr.append(buf)
    else:
        students_obr.append(buf)

quick_sort(countries)
quick_sort(countries_no_obr)
#print(countries)
#print(countries_no_obr)

#print()
quick_sort(students_obr)
quick_sort(students_no_obr)
#print(students_obr)
#print(students_no_obr)

kuda_go = {}

def f(students , countries):
    last_privlek = math.inf

    start_countr = 0
    for stud in students:
        for i in range(start_countr , len(countries)):
            country = countries[i]
        #for country in countries:

            now_privlek = country['id']

            if(stud['dohod'] < country['dohod']):
                #thapisivaem v last countru
                
                #if(last_privlek != math.inf ):
                #    kuda_go.update({stud['id'] : last_privlek})

                break

            start_countr = start_countr + 1
            if(now_privlek < last_privlek):
                last_privlek = now_privlek

        if(last_privlek != math.inf ):
                    kuda_go.update({stud['id'] : last_privlek})


f(students_no_obr , countries_no_obr)
f(students_obr , countries)

#print(kuda_go)

def send_parent(students ):
    for stud in students:
        #print("send parent" , stud['id'])

        now_parent = stud['parent']
        if(now_parent == 0 or not( now_parent in can_parent_countru_nums)  ):
            continue
        
        #print("send parent" , stud['id'])
        now_country = math.inf
        if(stud['id'] in kuda_go):
            now_country = kuda_go[stud['id']]

        kuda_go.update({stud['id'] : min(now_country , now_parent)})

send_parent(students_no_obr)
send_parent(students_obr)
#print(kuda_go)


answ = []
for i in range(q):
    id = i + 1
    if(id in kuda_go):
        answ.append(str(kuda_go[id]))
    else:
        answ.append(str(0))
        

fout.write(" ".join(answ))
fin.close()
fout.close()
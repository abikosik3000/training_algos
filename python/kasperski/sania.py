import sys 

lines = [] # список из построчных команд
id = 0 # переменная для создания id функций
perms = {} #словарь значений глобальных переменных
functions = {} #словарь имён функций и (их айди в качестве значения, номер строки, где они объявлены)
local_verbs = [] # список, где индекс каждого элемента соответствует id функции, а значение - словарю локальных переменных
num = 0 # индекс обрабатываемой строки в потоке команд

def retv(term, ff = False, id = 0):
    global perms
    global local_verbs
    if not ff:
        if term in perms.keys():
            return perms[term]
        else:
            return int(term)
    else:
        if term in local_verbs[id].keys():
            return local_verbs[id][term]
        else:
            return int(term)

def command(line): # обработка команд в глобальной области видимости
    line = list(line.split())
    global id
    global perms
    global functions
    global local_verbs
    global num
    global lines
    if line[0] == 'init':
        perms[line[1]] = retv(line[2])
    elif line[0] == 'add':
        perms[line[1]] = perms[line[1]] + retv(line[2])
    elif line[0] == 'sub':
        perms[line[1]] = perms[line[1]] - retv(line[2])
    elif line[0] == 'mul':
        perms[line[1]] = perms[line[1]] * retv(line[2])
    elif line[0] == 'div':
        perms[line[1]] = perms[line[1]] // retv(line[2])
    elif line[0] == 'function':
        functions[line[1]] = (id, num)
        dictt = {}
        for i in range(2, len(line)):
            dictt[line[i]] = None
        local_verbs.append(dictt)
        while line[0] != 'return':
            num += 1
            line = list(lines[num].split())
        id += 1
    elif line[0] in functions.keys():
        perms[line[1]] = fun_calc(line[0], line[1:], False, 0)
    elif line[0] == 'return':
        return perms[line[1]]
    elif line[0] == 'end_program':
        return 's'
    
def fun_calc(fun_name, args, flagg, idd): #вычисление значения функции
    global lines
    global functions
    global local_verbs
    global perms
    pos = functions[fun_name][1] + 1
    line = list(lines[pos].split())
    id = functions[fun_name][0]
    for x, y in zip(local_verbs[id].keys(), args):
        local_verbs[id][x] = retv(y, flagg, idd)
    while line[0] != 'return':
        if line[0] == 'init':
            local_verbs[id][line[1]] = int(retv(line[2], True, id))
        elif line[0] == 'add':
            local_verbs[id][line[1]] = local_verbs[id][line[1]] + retv(line[2], True, id)
        elif line[0] == 'sub':
            local_verbs[id][line[1]] = local_verbs[id][line[1]] - retv(line[2], True, id)
        elif line[0] == 'mul':
            local_verbs[id][line[1]] = local_verbs[id][line[1]] * retv(line[2], True, id)
        elif line[0] == 'div':
            local_verbs[id][line[1]] = local_verbs[id][line[1]] // retv(line[2], True, id)
        elif line[0] in functions.keys():
            local_verbs[id][line[1]] = fun_calc(line[0], line[1:], True, id)
        pos += 1
        line = list(lines[pos].split())
    return local_verbs[id][line[1]]

def solution(f_in, f_out):
    global lines
    global num
    res = None
    for line in f_in:
        line = line.rstrip("\n")
        if line == 'end_program':
            break
        if line != '':
            lines.append(line)
    while num < len(lines):
        line = lines[num]
        res1 = command(line)
        if res1 != None:
            if res1 != 's':
                res = res1
            else:
                break
        num += 1
    f_out.write(str(res))

if __name__ == "main":
    solution(sys.stdin, sys.stdout)
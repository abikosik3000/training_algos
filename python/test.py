fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

#n = int(fin.readline().rstrip())

def function(ages , intervals):

    max_age = max(ages)
    d = {  x : 0  for x in range(max_age + 2)}

    for age in ages:
        d[age] = d[age] + 1
    sum_left = 0
    for k,v in d.items():
        d[k] = sum_left
        sum_left = sum_left + v

    answ = [0] * len(intervals)
    for i in range(len(intervals)):

        if(intervals[i][0] > max_age or intervals[i][1] < 0):
            answ[i] = 0
            continue
        
        if(intervals[i][1] > max_age):
            answ[i] = d[max_age + 1] - d[intervals[i][0]]
            continue

        if(intervals[i][0] < 0):
            answ[i] = d[max_age + 1]
            continue

        answ[i] = d[intervals[i][1] + 1] - d[intervals[i][0]]
        
    return answ
        

a = [[1, -7], [0, 56], [2, 2]]
print( function([2,3,8,2,7,5,8,2,7] , a) )
#fout.write(str(biggest_combo))

fin.close()
fout.close()
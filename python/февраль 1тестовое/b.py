import bisect

def sort(array):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')


buf = [int(num) for num in fin.readline().rstrip().split(" ")] 
n = buf[0]
x = buf[1]
t = buf[2]

skylpt= [int(num) for num in fin.readline().rstrip().split(" ")] 

min_t_list = []
num_skylpt = []
for i in range(n):
    now_t = abs(x - skylpt[i])
    index = bisect.bisect_left(min_t_list,now_t)
    min_t_list.insert(  index , now_t)
    num_skylpt.insert(  index , i)
    #min_t_list.append( abs(x - el) )

#print(min_t_list)
#print(num_skylpt)

colv = 0
answ = []
for i in range(n):
    need_t = min_t_list[i]
    if(t - need_t >= 0):
        t = t - need_t
        colv = colv + 1
        answ.append( str(num_skylpt[i] + 1))

fout.write(str(colv)+'\n')
fout.write(" ".join(answ))
fin.close()
fout.close()
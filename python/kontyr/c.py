'''
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
buff = [ int(x) for x in fin.readline().rstrip().split(" ") ]
n = buff[0]
k = buff[1]
 
a = [ int(x) for x in fin.readline().rstrip().split(" ") ]
pref_sum_include = [0] * (n + 1)
'''
buff = [ int(x) for x in input().rstrip().split(" ") ]
n = buff[0]
k = buff[1]
 
a = [ int(x) for x in input().rstrip().split(" ") ]
pref_sum_include = [0] * (n + 1)
 
 
sum_a = 0
for i in range(n):
    sum_a = sum_a + a[i]
    pref_sum_include[i + 1] = sum_a
 
#print(a)
#print(pref_sum_include)
 
#[right] - [left - 1]
right_pos = 0
count_interes = 1
kount_nul = 0
for left in range(n):
 
    #if(a[left] == 0 and left != 0):
    #        kount_nul = kount_nul  - 1
    if(left == right_pos):
        count_interes = count_interes - 1
 
    for right in range(right_pos,n):
        print(left , right , kount_nul)
        
        right_pos = right
        sum_l = pref_sum_include[right + 1] - pref_sum_include[left] 
        if(a[right] == 0 ):
            kount_nul = kount_nul  + 1
        if(kount_nul > 1):
            kount_nul = 1
            break
        if(sum_l > k):
            break
 
        print('yes')
        
        count_interes = count_interes + 1
    
    kount_nul = kount_nul - 1
    count_interes = count_interes + 1

print(str(count_interes - 1))
#print( str(max_i + 1)+" "+str(min_i + 1) )
#fout.write( "".join(map(str,answ)) )
#fout.close()
#fin.close()
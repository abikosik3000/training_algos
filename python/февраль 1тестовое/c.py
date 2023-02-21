fin = open('input.txt' , 'r')
fout = open('output.txt' , 'w')

k = int( fin.readline().rstrip() )
#const
plt = [int(num) for num in fin.readline().rstrip().split(" ")] 


optimal_deals_right = [None] * k
optimal_deals_left = [None] * k 
#ВКЛЮЧИТЕЛЬНО ВКЛЮЧИТЕЛЬНО
# ret start fin koef=1 is_deal
def optimal_deal_k(i_start , i_fin ):

    global_max = plt[i_fin]
    max_index = i_fin
    buy_index = None

    save_buy = None
    save_sell = None

    max_k = 1
    for i in range(i_fin ,i_start - 1, -1 ):
        now_cost = plt[i]

        now_k = global_max / now_cost
        if(now_k > max_k):
            max_k = now_k
            save_buy = i
            save_sell = max_index

        if(now_cost > global_max):
            global_max = now_cost
            max_index = i

        deal = not( save_buy is None )
        #answ = ''
        
        optimal_deals_right[i]  = (max_k , deal ,save_buy , save_sell ) 

def optimal_deal_k_1(i_start , i_fin ):

    global_min = plt[i_start]
    min_index = i_start
    sel_index = None

    save_buy = None
    save_sell = None

    max_k = 1
    for i in range(i_start , i_fin + 1 ):

        now_cost = plt[i]

        if(now_cost < global_min):
            global_min = now_cost
            min_index = i

        now_k = now_cost / global_min
        if(now_k > max_k):
            max_k = now_k
            save_buy = min_index
            save_sell = i

        

        deal = not( save_buy is None )
        #answ = ''
        
        optimal_deals_left[i]  = (max_k , deal ,save_buy , save_sell  ) 



optimal_deal_k(0 , k-1 ) 
optimal_deal_k_1(0,k-1)

optimal_deals_right.append((1 , False , None , None) )
max_k = 1
answ = []
for i in range(0 , k):
    rez_1 = optimal_deals_left[i]
    rez_2 = optimal_deals_right[i + 1]

    now_k = rez_1[0] * rez_2[0] 
    if(now_k > max_k):
        max_k = now_k
        answ = []
        if(rez_1[1] ):
            answ.append(str(rez_1[2] + 1)+" "+str(rez_1[3] + 1))
        if(rez_2[1] ):
            answ.append(str(rez_2[2] + 1)+" "+str(rez_2[3] + 1))



#print(optimal_deals_right)
#print()
#print(optimal_deals_left)
'''
max_k = 1
answ = []
for i in range(k // 2 + 1):
    rez_1 = optimal_deal_k(0 , i )
    rez_2 = optimal_deal_k(i , k-1 ) 
    #print(rez_1 ,  rez_2)
    now_k = rez_1['k'] * rez_2['k'] 
    if(now_k > max_k):
        max_k = now_k
        answ = []
        if(rez_1['deal'] ):
            answ.append(rez_1['answ'])
        if(rez_2['deal'] ):
            answ.append(rez_2['answ'])
'''
fout.write(str(len(answ))+"\n")
fout.write("\n".join(answ))
fin.close()
fout.close()

'''
##DEL
abs_plt = []
abs_plt.append(0)
for i in range(1,k):
    abs_plt.append(plt[i] - plt[i - 1])
    
print(abs_plt)
'''
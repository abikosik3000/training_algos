#fin = open('input.txt', 'r')
#fout = open('output.txt', 'w')

n = int(input().rstrip())
s = input().rstrip()

def chek_has(s):
    d = set()
    for x in s:
        d.add(x)
    return (len(d) == 4)

def len_substr(d):
    l = 0
    for v in d.values():
        l += v
    return l

def has_s_good(d):
    for v in d.values():
        if(v == 0):
            return False
    return True

if(chek_has(s)):
    
    left = 0
    #right = 0
    d_sub = { 'a':0 , 'b':0 ,'c':0 ,'d':0 }
    min_sub = n
    for i in range(n):
        d_sub[s[i]] += 1
        while( has_s_good(d_sub)):
            min_sub = min(min_sub, i - left + 1)
            d_sub[s[left]] -= 1
            left += 1

    print(min_sub)
else:
    print(-1)

#fout.close()
#fin.close()
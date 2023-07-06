def l_binsearch(l, r, check, checkparams): # ____*----
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1  #можно выкинуть плохое значение 
    return l

def r_binsearch(l, r, check, checkparams): # -----*____
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1 
    return l
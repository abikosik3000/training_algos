def chek_skob(s):
    stak = []
    open_to_close = {'(' : ')', '[' : ']' , '{' : '}' }
    close = (')',']','}')
    for symb in s:
        if(symb in open_to_close):
            stak.append(open_to_close[symb])
        if(symb in close):
            if(len(stak) == 0):
                return False
            if(stak.pop() != symb):
                return False
    return (len(stak) == 0)

print( "Nice" if chek_skob(input()) else "Bruh" )
x = 0
try: print(x/0)
except ZeroDivisionError:
    print(x+1, sep='')
except ZeroDivisionError:
    print(x+2, sep='')
except ZeroDivisionError:
    print(x+3, sep='')
import functools
import time

def cash_f( f ):
    
    hash_args = dict()

    def _decorate(*args , **kvargs):
        
        if( hash( args ) in hash_args):
            return hash_args[args]
        else:
            ret = f( *args , **kvargs)
            hash_args.update({hash( args ) : ret})
            return ret
    
    return _decorate


@cash_f
def f(lenght):
    iteraror = (x for x in range(0,lenght , 2))
    return list(iteraror)

@abs
class animal:
    def __animal__():
        pass    

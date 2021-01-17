from typing import Callable, Any
from operator import eq, mod
from functools import wraps, partial

def Compose(*funcs):
    def inner(args):
        state = args
        for func in reversed(funcs):
            state = func(state)
        return state
    return inner

def is_int(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, int) else val

    return inner

@is_int
def Queijo(n: int) -> str:
    return 'Queijo' if eq(mod(n, 3), 0) else n

@is_int
def Queijo_Goiabada(n: int) -> str:
    return 'Romeu e Julieta' if eq(mod(n, 3), 0) and eq(mod(n, 5), 0) else n

@is_int
def Goiabada(n: int) -> str:
    return 'Goiabada' if eq(mod(n, 5), 0) else n

'''def RomeuEJulieta(val: int):
    if Queijo_Goiabada(val) == 'Romeu e Julieta':
        return 'Romeu e Julieta'

    if Queijo(val) == 'Queijo':
        return 'Queijo'
    
    if Goiabada(val) == 'Goiabada':
        return 'Goiabada' '''

RomeuEJulieta = Compose(Goiabada, Queijo, Queijo_Goiabada)
RomeusEJulietas = Compose(list, partial(map, RomeuEJulieta))
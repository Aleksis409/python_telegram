# задача 3-4

from functools import cache
@cache
def fib(n: int) -> int:
    # print(f'fib({n})')
    if n == 0:
        return 0
    if n == 1:
        return 1    
    return fib(n-1) + fib(n-2)

print(fib(50))

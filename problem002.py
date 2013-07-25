import math
from tools import memoized

def fibonnaci(n):
    A = math.pow((1 + math.sqrt(5)) / 2, n)
    B = math.pow((1 - math.sqrt(5)) / 2, n)
    return (1/math.sqrt(5)) * ( A - B )

def fib(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 1
    return fib(n-1) + fib(n-2)

@memoized
def memfib(n): 
    if (n == 1):
        return 1
    if (n == 0):
        return 1
    return memfib(n-1) + memfib(n-2)   

def problem002():
    sum = 0
    val = 0
    i = 0
    while (val < 4000000):
        val = int(fibonnaci(i))
        if val % 2 == 0:
            sum += val
        i += 1
    print sum
        
# Fib sequence is odd, odd, even, so can just compute every 3rd entry



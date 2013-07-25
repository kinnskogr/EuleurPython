from math import factorial
from tools import memoized

@memoized
def npaths(cols, rows):
    opts = 0
    if rows == 0 and cols == 0:
        return 1

    if cols >= 0:
        opts += npaths(cols-1, rows)
    if rows >= 0:
        opts += npaths(cols, rows-1)

    return opts


def problem015a(cols = 20, rows = 20):
    """Let's use pascal's triangle with 2*20 choose 20"""
    answer = factorial(cols + rows) / (factorial(cols) * factorial(rows))
    
    print "There are %s paths" % answer

def problem015b(cols = 20, rows = 20):
    """Let's use memoization. It should turn the quadratic problem into a linear problem"""
    answer = npaths(cols, rows)

    print "There are %s paths" % answer


if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem015a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem015b)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

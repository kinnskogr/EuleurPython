"""
Find the sum of all the primes below two million.
"""

import tools
import math

limit = 2000000
#limit = 20000

def problem010a():
    l = tools.quick_sieve(limit)
    print sum(l)

def problem010b():
    l = tools.sieve_eratosthenes(limit)
    print sum(l)

def problem010c():
    l = tools.filter_primes(range(2,limit))
    print sum(l)
    
if __name__ == "__main__":
    import timeit

    t = timeit.Timer(problem010a)
    print "Solution a: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    # t = timeit.Timer(problem010b)
    # print "Solution b: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem010c)
    print "Solution c: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

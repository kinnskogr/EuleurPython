from problem002 import memfib, fibonnaci
import math

def problem025a():
    fib = 0
    i = -1
    while len(str(fib)) < 1000:
        i += 1
        #print i
        fib = int(memfib(i))
        #print len(str(fib))

    print "index %s with value %s" % (i, fib)


## Should be able to get around the overflow error by working in logs, then converting back to exp
def logfib(n):
    #   A = math.pow((1 + math.sqrt(5)) / 2, n)
    #   B = math.pow((1 - math.sqrt(5)) / 2, n)
    #   fib = (1/math.sqrt(5)) * ( A - B )
    #
    #For large n, can drop 2nd term, so:
    #   fib = A / math.sqrt(5)
    #   log(fib) = log(A) - log(math.sqrt(5))
    #            = n * log( 1 + math.sqrt(5) / 2) - log(math.sqrt(5))
    
    A = n * math.log( (1 + math.sqrt(5)) / 2) 
    A -= math.log(math.sqrt(5))
    return math.exp(long(A))
# Still fails b/c math.exp uses float!
# Can solve numerically:
# fib(n) > 10**999
# A > 999 * 10
# n  > 9990 + log(sqrt(5)) / log( (1+sqrt(5)) / 2) ??
    
def problem025b():
    fib = 0
    i = -1
    while len(str(fib)) < 1000:
        i += 1
        fib = int(logfib(i))
    print "index %s with value %s" % (i, fib)

if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem025a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        

    t = timeit.Timer(problem025b)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        


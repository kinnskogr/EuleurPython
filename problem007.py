import tools

def problem007():
    """prime number theorem says # primes < n = n / ln n + B, B = 1.0836 --> nPrimes ~ n / ln n
    Solving in reverse: e^(-1 *  ProductLog(-1, -(1/a))) --> a ~ 116684
    """

    n = 10001
    r = range(116684)
    print r[-1]
    l = tools.filter_primes(r)
    print l[n]
    
if __name__ == "__main__":
    import timeit

    t = timeit.Timer(problem007)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

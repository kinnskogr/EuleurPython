from tools import memoized

def sequence(n):
    orig = n
    if n <= 1:
        return 0
    
    tries = 0
    while n != 1:
        tries += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1

    #print orig, tries
    return tries

def rsequence(n, i = 0):
    if n <= 1:
        return i
    
    if n % 2 == 0:
        return rsequence(n/2, i+1)
    else:
        return rsequence(3*n + 1, i+1)

@memoized
def msequence(n):
    return sequence(n)

def problem014a(max_int = 1000000):
    index = 2
    ntries = 1
    for i in range(max_int / 2 + 1, max_int+1):
        test = sequence(i)
        if test > ntries:
            ntries = test
            index = i
    print "%s with %s" % (index, ntries)

def problem014b(max_int = 1000000):
    index = 2
    ntries = 1
    for i in range(max_int / 2 + 1, max_int+1):
        test = rsequence(i)
        if test > ntries:
            ntries = test
            index = i
    print "%s with %s" % (index, ntries)
    
def problem014c(max_int = 1000000):
    index = 2
    ntries = 1
    for i in range(max_int, max_int / 2, -1):
        test = msequence(i)
        if test > ntries:
            ntries = test
            index = i
    print "%s with %s" % (index, ntries)

if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem014a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem014b)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem014c)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

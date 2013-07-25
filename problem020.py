import math

def problem020a():
    output = sum(int(i) for i in str(math.factorial(100)))
    print "The sum is %s" % output

if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem020a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        


"""Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

limit = 10000

def problem006a():
    """
    A = Sum(x_i)^2 = (x_0 + x_1 +...)^2 = x_0^2 + x_0*x_1 + ... + x_1^2 + x_1*x_0 + ...
    B = Sum(x_i^2) = x_0^2 + x_1^2 + ...
    A - B = 2*x_0*x_1 + 2*x_0*x_2 + ...
    """
    output = 0
    i = 1
    while i <= limit:
        j = i+1
        while j <= limit:
            output += 2*i*j
            j += 1
        i += 1

    print output
    return output

def problem006b():
    """
    Same as above, but more pythonic
    """
    output = sum([2*x*y for x in range(1, limit+1) for y in range(x+1, limit+1)])
    print output
    return output

def f_sum(n):
    """Arithmetic progession"""
    return n*(n+1)/2

def f_sumsq(n):
    """Using an ansatz"""
    return (2*n+1) * (n+1) * n / 6

def problem006c():
    """
    Using math!
    """

    output = pow(f_sum(limit),2) - f_sumsq(limit)
    print output
    return output

def problem006d():
    """
    Brute force
    """
    
    output = sum(range(limit+1))**2  - sum([x**2 for x in range(limit+1)])
    print output
    return output

if __name__ == "__main__":
    import timeit

    t = timeit.Timer(problem006a)
    print "Solution a: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem006b)
    print "Solution b: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem006c)
    print "Solution c: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem006d)
    print "Solution d: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

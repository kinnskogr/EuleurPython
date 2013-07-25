"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def problem009a():
    """
    a = sqrt(c^2 - b^2)
    """
    
    for c in range(3, 1000):
        for b in range(2, c):
            a = math.sqrt(c**2 - b**2)
            if a > b:
                continue
            if a + b + c != 1000:
                continue
            print a,b,c
            print a*b*c
            return            

def problem009b():
    """
    a^2 + b^2 = c^2
    a + b + c == 1000
    -->
    b==(1000-c)/2+1/2 Sqrt[-1000000+2000 c+c^2])

    -1000000+2000 c+c^2 == 0 for c = 414.214
    """
    
    for c in range(415, 1000):

        b = (1000.-c)/2
        b += math.sqrt(c**2 + (2000.*c) - 1000000) / 2

        a = 1000. - c - b

        if b < 0 or a < 0:
            continue
        if b != int(b) or a != int(a):
            continue

        print a,b,c
        print a*b*c
        return         
    
def problem009c():
    
    for c in range(3,1000):
        for b in range(2, c):
            for a in range(1,b):
                if a**2 + b**2 != c**2:
                    continue
                if a + b + c != 1000:
                    continue
                print a,b,c
                print a*b*c
                return


if __name__ == "__main__":
    import timeit

    t = timeit.Timer(problem009a)
    print "Solution a: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem009b)
    print "Solution b: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem009c)
    print "Solution c: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

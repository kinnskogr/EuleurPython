"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.  Find
the largest palindrome made from the product of two 3-digit numbers.
"""

from tools import reverse, factorize

def isPalindrome(num):
    n = str(num)
    return False not in [n[i] == n[len(n) - 1 - i] for i in range(len(n))]

def problem004a():
    """Brute force"""

    #palindromes = map(lambda x: [x*i for i in range(x,1000)], [i for i in range(100, 1000)])
    #palindromes = reduce(lambda x,y: x+y, palindromes)
    #palindromes = [i for i in palindromes if isPalindrome(i)]
    
    palindromes = [x*y for x in range(100, 1000) for y in range(x, 1000) if isPalindrome(x*y)]

    print sorted(palindromes)[-1]

def problem004b():
    """
    Palindrome = XYZZYX
    P = 100001 X + 10010 Y + 1100 Z
    P = 11(9091 X + 910 Y + 100 Z)
    """

    palindromes = [x*y for x in range(990, 110-1, -11) for y in range(x, 1000) if isPalindrome(x*y)]
    print max(palindromes)

    # output = 0
    # for x in range(990, 110-1, -11):
    #     for y in range(x, 1000):
    #         if isPalindrome(x*y) and x*y > output:
    #             output = x*y
    # print output

def problem004c():
    """Just count down till we find a palindrome because we know
    100001 (smallest palindrome) < P < 999*999
    """

    output = 999*999
    while output > 100001:
        if output == reverse(output):
            #There must be a cleaner way to perform this test
            test = [output / x for x in range(100,1000) if 
                    output/x > 100 and 
                    output/x < 999 and 
                    float(output)/x == output/x]
            if len(test):
                print output
                break
        if output == 906609:
            break
        output -= 1
        
    return output


if __name__ == "__main__":
    import timeit
    t = timeit.Timer(problem004a)
    print "Solution a: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem004b)
    print "Solution b: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)

    t = timeit.Timer(problem004c)
    print "Solution c: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)



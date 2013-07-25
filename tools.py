def gcd(a,b):
    """Greatest Common Denominator"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    """Least Common Multiple"""
    return a * b / gcd(a, b)


def factorize(num):
    """Return all the factors for a number"""
    from math import ceil

    powers = []
    limit = int(ceil(float(num)/2)) # we only need to look up to num/2 for factors
    for i in range(2, limit+1):
        while num % i == 0: # ie, if i is a factor of num
            powers.append(i)
            num = num/i # take factor out of num and continue with smaller num
    if len(powers) == 0: # haven't found any factors, ie, num is prime
        powers.append(num)
    return powers

def filter_primes(primes = range(1,20), i=2):
    """Find primes in a range using the Sieve of Eratosthenes
    http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""

    if i**2 < primes[-1]:
        primes[i:] = filter(lambda x: x % i, primes[i:])
        return filter_primes(primes, i+1)
    else:
        return primes

def sieve_eratosthenes(limit):
    """ Return all the primes below (NOT INCLUDING) the specified limit. """
 
    numbers = range(2,limit)
    primes = []
 
    while True:
        if len(numbers) == 0:
            break
 
        prime = numbers[0]
        primes.append(prime)
        multiples = []
 
        for n in numbers:
            if n % prime == 0:
                multiples.append(n)
 
        for n in multiples:
            numbers.remove(n)
 
    return primes

def quick_sieve(limit):
    arr = [True] * limit
    
    # for i in range(2, limit/2):
    #     for j in range(i*2, limit, i):
    #         arr[j] = False

    def func(x):
        for i in range(x*2, limit, x):
            arr[i] = False
            
    map(func, range(2, limit/2))
    
    return filter(lambda x: arr[x], range(2,limit))


def reverse(num):
    """Reverse an integer, ie. 123 --> 321"""

    num = int(num)
    output = 0
    while num > 0:
        output = 10 * output + (num % 10)
        num = num / 10

    return output

def strReverse(s):
    """Python sequence slice addresses can be written as
    a[start:end:step] and any of start, stop or end can be 
    dropped"""

    return str(s)[::-1]

class memoized(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            return self.func(*args)

    def __repr__(self):
        return self.func.__doc__
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


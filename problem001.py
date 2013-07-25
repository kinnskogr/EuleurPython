def problem001():
    """If we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    sum = 0
    for i in range(199):
        i += 1
        if i % 3 == 0:
            continue
        sum += i*5;
    for i in range(333):
        i += 1
        sum += i*3
    print sum

    sum = 0
    for i in range(999):
        i += 1
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    print sum

    print reduce(lambda x,y: x+y, filter(lambda n: n%3==0 or n%5==0, range(1000)))
    #arithmetic progressions
    #http://en.wikipedia.org/wiki/Arithmetic_progression
    x = 1000;
    print 1.5*(int)((x-1)/3)*(int)((x+2)/3) + 2.5*(int)((x-1)/5)*(int)((x+4)/5) - 7.5*(int)((x-1)/15)*(int)((x+14)/15);


for x in dir():
    if not "problem" in x:
        continue

    print "------------"
    print x
    exec "%s()" % x


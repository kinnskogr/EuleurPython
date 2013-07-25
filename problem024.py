from math import factorial

def permute(digits):
    #print "permute %s" % digits
    order = len(digits)
    if order == 1:
        return digits

    output = []
    for i in range(order):
        for j in permute( digits[0:i] + digits[i+1:order]):
            #print" append %s to %s" % (j, digits[i])
            output.append( digits[i] + j )
            #print " %s" % output

    return output
        

def problem024a():
    """
    Brute force
    """
    
    values = [int(i) for i in  permute(['0','1','2', '3', '4', '5', '6', '7', '8', '9'])]
    print values[int(1E6)-1]

def problem024b():
    """
    We know that for each leading index, there are (N-1)!
    combinations. The lowest ones will start with 0, then 1, etc...
    
    9! = 362880, 1E6 / 362880 = 2.76, so we'll go through 2 full
    cycles (0 and 1 leading) and will be 3/4 of the way through the
    third cylce (2 leading). Should be able to make our way down the
    chain like that.
    
    Need to reduce the target by 1. Check it out. If target = 1, then
    answer = 0123456798, where expected to end with 89. Makes sense,
    since target should really be called remainder.
    """
    
    values = ['0','1','2', '3', '4', '5', '6', '7', '8', '9']
    target = 1E6 - 1

    order = len(values) - 1
    answer = ""
    
    while order+1 > 0:

        cycles = int(target / factorial(order))
        target -= cycles * factorial(order)
        answer += values[cycles]
        del(values[cycles])
        order = len(values)-1
        
    print answer
    


if __name__ == "__main__":
    import timeit


    # t = timeit.Timer(problem024a)
    # print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        

    t = timeit.Timer(problem024b)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        


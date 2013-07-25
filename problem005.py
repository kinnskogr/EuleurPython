import problem003
import tools

def problem005(divisors = range(1,21)):
    # output = 1
    # for d in divisors:
    #     output = tools.lcm(output, d)
    # print output

    # Better yes, use reduce!
    print reduce(tools.lcm, range(1,21))

def problem005c(divisors = range(1, 21)):

    divisors.sort()

    print divisors

    output = divisors[-1]

    while(True):
        all_good = True
        for d in divisors:
            if output % d != 0:
                all_good = False
                break
        if all_good:
            break
        output += divisors[-1]

    print output

def problem005a(low = 1, high = 10):
    divisors = range(low, high+1)
    print divisors
    output = 1
    for d in divisors:
        output *= d
    print output

    primes = []
    for d in divisors:
        l = problem003.find_primes(d)
        primes.extend(l)

#    primes =  set(primes)
 
    print sorted(primes)
    print set(primes)
    output = 1
    for p in primes:
        output *= p
    print output

    output = 1
    for d in divisors:
        output *= d
    print output
    divisors = problem003.find_divisors(output)

    output = []

    divisors = sorted(divisors)
    print divisors

    for i in range(len(divisors)):
        is_common = False
        for j in range(i+1, len(divisors)):
            if divisors[j] % divisors[i] == 0:
                is_common = True
                break
        if not is_common:
            output.append(divisors[i])
    print len(output)

    divisors = output
    print divisors

    output = 1
    for d in divisors:
        output *= d
    print output
                

    return

    output = high
    while (True):
        all_good = True

        for d in divisors:
            if output % d != 0:
                all_good = False
                break

        if all_good == True:
            print "!!!",output
            break
        else:
            output += 1


if __name__ == "__main__":
    problem005()

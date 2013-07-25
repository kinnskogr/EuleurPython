import math

def find_divisors(n):
    output = []
    square = int(math.sqrt(n))
    #square = n-1
    while (square > 1):
        if n % square == 0:
            output.append(square)
        square -= 1

    return output

# def find_divisors(n):
#     output = []
#     square = int(math.sqrt(n))
    
#     #No need to check EVERY number, even ones clearly won't be prime

#     if (square %2 == 0):
#         output.append(square)
#         square -= 1

#     while (square > 1):
#         if n % square == 0:
#             output.append(square)
#         square -= 2
#     return output


def find_primes(n):
    output = []
    values = find_divisors(n)
    if len(values) == 0:
        return [n]

    for v in values:
        output.extend(find_primes(v))

    return output
    
def problem003(n = 600851475143):
    print set(find_primes(n))
        

if __name__ == "__main__":
    problem003()

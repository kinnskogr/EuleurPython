from problem018 import reverse_sum

data = open("problem067_triangle.txt", "r").readlines()
triangle = []

for line in data:
    triangle.append(
        [int(i) for i in line.strip().split()]
        )

def problem067a():
    reverse_sum(triangle)


if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem067a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    


    



names = open('problem022_names.txt', 'r').read().strip("\n").split(",")
offset = ord('A') - 1

def sum_of_chars(name):
    output = sum(name, lambda x, y: x + ord(y) - offset)

def problem022a():
    loc_names = sorted(names)
    
    numerical_values = [
        (index+1) * reduce(lambda x, y: x + ord(y) - offset, name, 0) 
        for index, name in enumerate(loc_names)
        ]

    #print numerical_values
    print sum(numerical_values)
    
    

if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem022a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)        

import copy
from tools import memoized

default_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]

def ordered_finder(triangle = default_triangle):
    output = []

    for (i, row) in enumerate(triangle):
        for (j, value) in enumerate(row):
            output.append( (i, j, value) )

    output = sorted(output, key = lambda x: x[2], reverse = True)

    return output

path = []

def max_path_finder(triangle, row, col, direction):
    if row < 0 or row >= len(triangle):
        return 0
    if col < 0 or col >= len(triangle[row]):
        return 0

    output = triangle[row][col]
    
    if direction in ["up", "both"]:
        vals = [(col+i, max_path_finder(triangle, row+1, col+i, "up")) for i in [0, 1]]
        loc = sorted(vals, key = lambda x: x[1], reverse = True)[0]
        output += loc[1]
        
    if direction in ["down", "both"]:
        vals = [(col + i, max_path_finder(triangle, row-1, col+i, "down")) for i in [0, 1]]
        loc = sorted(vals, key = lambda x: x[1], reverse = True)[0]
        output += loc[1]

    return output

@memoized
def mem_max_path_finder(triangle, row, col, direction):
    if row < 0 or row >= len(triangle):
        return 0
    if col < 0 or col >= len(triangle[row]):
        return 0

    output = triangle[row][col]
    
    if direction in ["up", "both"]:
        vals = [(col+i, mem_max_path_finder(triangle, row+1, col+i, "up")) for i in [0, 1]]
        loc = sorted(vals, key = lambda x: x[1], reverse = True)[0]
        output += loc[1]
        
    if direction in ["down", "both"]:
        vals = [(col + i, mem_max_path_finder(triangle, row-1, col+i, "down")) for i in [0, 1]]
        loc = sorted(vals, key = lambda x: x[1], reverse = True)[0]
        output += loc[1]

    return output

def reverse_sum(triangle):
    values = copy.copy(triangle)
    for row in range(len(values)-1, 0, -1):
        for col in range(len(values[row])-1):
            values[row-1][col] += max(values[row][col:col+2])

    print values[0][0]

def problem017a():
    ordered_pairs = ordered_finder(default_triangle)

    sums = []
    for row, col, val in ordered_pairs:
        if val >= 70:
            sums.append(max_path_finder(default_triangle, row, col, "both"))

    print max(sums)    

def problem017b():
    print max_path_finder(default_triangle, 0, 0, "both")

def problem017c():
    print mem_max_path_finder(default_triangle, 0, 0, "both")

def problem017d():
    reverse_sum(default_triangle)

if __name__ == "__main__":
    import timeit
    
    t = timeit.Timer(problem017a)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem017b)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem017c)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    

    t = timeit.Timer(problem017d)
    print "Solution: %.2f usec/pass" % (1000000 * t.timeit(number=1)/100000)    



default_data = "319\n\
680\n\
180\n\
690\n\
129\n\
620\n\
762\n\
689\n\
762\n\
318\n\
368\n\
710\n\
720\n\
710\n\
629\n\
168\n\
160\n\
689\n\
716\n\
731\n\
736\n\
729\n\
316\n\
729\n\
729\n\
710\n\
769\n\
290\n\
719\n\
680\n\
318\n\
389\n\
162\n\
289\n\
162\n\
718\n\
729\n\
319\n\
790\n\
680\n\
890\n\
362\n\
319\n\
760\n\
316\n\
729\n\
380\n\
319\n\
728\n\
716"

def problem079a(data = None):
    logger = {}

    for line in data.split("\n"):
        for i in range(len(line)-1, -1, -1):
            #print line
            #print i, line[i]
            vals = logger.get(line[i], set([]))

            for j in range(i-1,-1, -1):
                #print "  ",j, line[j]
                vals.update(line[j])
            logger[line[i]] = vals

    for key, val in sorted(logger.items(), cmp = lambda x,y: cmp(len(y[1]), len(x[1]))):
        print key, len(val), val

def problem079b(data = None):
    data = [[i for i in l] for l in data.split()]

    output = ""
    
    while len(data) > 0:
        vals = {}
        for line in data:
            val = vals.get(line[0], 0)
            val += 1
            vals[line[0]] = val
        
        key =  sorted(vals.items(), cmp = lambda x,y: cmp(y[1], x[1]))

        print key

        key = key[0][0]

        output += key

        for line in data:
            if line[0] == key:
                line.remove(key)
        
        while True:
            try:
                data.remove([])
            except ValueError:
                break

    print output

if __name__ == "__main__":
    problem079a(default_data)
    
    problem079b(default_data)
    


filenames = ["input1.txt", "input2.txt"]


for filename in filenames:

    # Part 1
    f = [s.strip().replace("  "," ").replace("  "," ").replace("  "," ").split(" ") for s in open(filename)]
    op = f[-1]
    vals = [[int(x) for x in line] for line in f[:-1]]
    
    acc = 0
    for c in range(len(op)):
        if op[c] == "+":
            tmp = 0
            for r in range(len(vals)):
                tmp += vals[r][c]
        if op[c] == "*":
            tmp = 1
            for r in range(len(vals)):
                tmp *= vals[r][c]
        #print("--%s--"%op)
        acc += tmp
    print(acc)

    
    # Part 2
    f = [s.replace(" ","0").strip() for s in open(filename)]

    columns = []
    ops = []
    ci = 0
    while ci < len(f[0]):
        ci_start = ci 
        ci_end = ci+1
        ops.append(f[-1][ci_start])
        while ci_end<len(f[-1]) and  not f[-1][ci_end] in "+*" :
            ci_end += 1
        #ci_end -= 1
        ci = ci_end

        vals = [0]*(ci_end-ci_start)

        for ri in range(len(f)-1):
            for cii in range(ci_start, ci_end):
                vals[cii-ci_start] += int(f[ri][cii])*10**(len(f)-ri)
        vals = [int(str(v).replace("0","")) for v in vals if v != 0]
        columns.append(vals)
    
    acc = 0
    for c in range(len(ops)):
        if ops[c] == "+":
            tmp = 0
            for v in columns[c]:
                tmp += v
        if ops[c] == "*":
            tmp = 1
            for v in columns[c]:
                tmp *= v
        #print("--%s--"%op)
        acc += tmp
    print(acc)


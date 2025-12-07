
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


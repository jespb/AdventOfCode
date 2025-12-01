
filenames = ["input1.txt", "input2.txt"]

for f in filenames:
    f = open(f)
    dial = 50 
    SIZE = 100
    count1 = 0
    count2 = 0

    for line in f:
        dir = line[0]
        step = int(line[1:].strip())

        full_spins = step//SIZE 
        step %= SIZE 

        old_ = dial
        dial += step if dir == "R" else -step 

        # Part 2 , lazy mode
        count2 += full_spins
        if dial != dial%SIZE:
            count2 += 1
        if dir == "L" and dial%SIZE == 0 and step != 0:
            count2 += 1
        if old_ == 0 and dir == "L":
            count2 -= 1
        
        dial %= SIZE 

        # Part 1
        if dial == 0:
            count1 += 1

    print(count1, count2)


filenames = ["input1.txt", "input2.txt"]

for filename in filenames[:]:
    mapa = [s.strip() for s in open(filename)]
    init_pos = mapa[0].index("S")
    layer = [0]*len(mapa[0])
    layer[init_pos] = 1
    splitters_used = 0
    for line in mapa[1:]:
        new_layer = [0]*len(mapa[0])
        splitters_usage = [0]*len(mapa[0])
        for i in range(len(layer)):
            if line[i]==".":
                new_layer[i] += layer[i]
            if line[i] == "^":
                if layer[i]>0:
                    splitters_usage[i] = 1
                new_layer[i+1] += layer[i]
                new_layer[i-1] += layer[i]
        layer = new_layer
        splitters_used += sum(splitters_usage)
    print(sum(layer), splitters_used)

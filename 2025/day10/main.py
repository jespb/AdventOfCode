
filenames = ["input1.txt", "input2.txt"]


def solved(target, commands, sol):
	#print(commands)
	target = target[:]
	for s in sol:
		for ind in commands[s]:
			target[ind]= (target[ind]+1)%2
	return sum(target)==0


for filename in filenames[:]:
	f = [s.strip().split(" ") for s in open(filename)]

	acc = 0
	for line in f:
		t = [1 if c=="#" else 0 for c in line[0][1:-1] ]
		commands = [eval(tup) for tup in line[1:-1]]
		commands = [ [c] if type(c)==int else list(c) for c in commands]

		sols = []
		toExplore = [[]]
		ok = solved(t, commands, toExplore[0])
		if ok:
			sols.append( [len(toExplore[0]), toExplore[0]])
		i = 0
		while i < len(commands):
			new_toExplore=[]
			for te in toExplore:
				new_toExplore.append( te + [i] )
			toExplore.extend(new_toExplore)
			#print("d", toExplore)

			for te2 in new_toExplore:
				ok = solved(t, commands, te2)
				if ok:
					sols.append( [len(te2), te2])
			i+=1

		sols.sort()
		acc+=sols[0][0]
	print(acc)
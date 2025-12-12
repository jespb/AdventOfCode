
filenames = ["input1.txt", "input2.txt"]


def solved(target, commands, sol):
	#print(commands)
	target = target[:]
	for s in sol:
		for ind in commands[s]:
			target[ind]= (target[ind]+1)%2
	return sum(target)==0



for filename in filenames[2:]:
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




def apply_f(commands, sol):
	base = [0]*len(commands[0])
	for si in range(len(sol)):
		cm = [v*sol[si] for v in commands[si]]
		for ind in range(len(cm)):
			base[ind] += cm[ind]
	return base

def valid_f(target, commands, sol, max_clicks):
	if sum(sol) > max_clicks:
		return -1

	base = apply_f(commands, sol)

	for si in range(len(base)):
		if base[si]>target[si]:
			return -1
	if base == target:
		return 1
	else:
		return 0



for filename in filenames[:]:
	f = [s.strip().split(" ") for s in open(filename)]

	acc = 0
	for line in f:
		print("---")
		t = [int(c) for c in line[-1][1:-1].split(",") ]
		commands = [eval(tup) for tup in line[1:-1]]
		commands = [ [c] if type(c)==int else list(c) for c in commands]

		tmp = []
		for c in commands:
			v = [0]*len(t)
			for i in c:
				v[i] = 1
			tmp.append(v)
		commands = tmp

		sols = [[0]*len(commands)]
		solutions = []
		max_d = 1000

		current_min = 20

		for i in range(len(commands)):
			new_sols = []
			for s in sols:
				s1 = s[:]
				bl = apply_f(commands, s1)

				valid = 0

				while valid != -1:
					valid = valid_f(t, commands, s1, current_min)
					if valid != -1:
						new_sols.append(s1[:])
					if valid == 1:
						solutions.append(s1[:])
						if sum(s1) < current_min:
							current_min = sum(s1)
					s1[i] += 1


			#print(new_sols)
			sols = new_sols
				
		compress = min([sum(s) for s in solutions])
		print(compress)

		acc += compress

	print(acc)
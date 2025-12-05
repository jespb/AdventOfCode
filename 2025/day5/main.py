
filenames = ["input1.txt", "input2.txt"]



for filename in filenames:

	# Part 1
	f = [s.strip() for s in open(filename)]
	lists = []
	s = f[0]
	i = 0
	while s != "":
		s = [int(a) for a in s.split("-")]
		lists.append(s)
		i+=1
		s=f[i]

	i+=1
	acc = 0
	while i<len(f):
		v = int(f[i])
		i+=1
		j = 0
		found = False
		while j<len(lists) and not found:
			found = v>=lists[j][0] and v<=lists[j][1]
			j+=1
		acc += 1 if found else 0
	print(acc) 



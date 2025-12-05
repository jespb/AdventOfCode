
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


	# Part 2
	f = [s.strip() for s in open(filename)]
	lists = []
	s = f[0]
	i = 0
	while s != "":
		s = [int(a) for a in s.split("-")]
		lists.append(s)
		i+=1
		s=f[i]

	old_n_list = -1
	n_list = len(lists)
	while n_list != old_n_list:
		for i in range(len(lists)):
			l = lists.pop(0)
			merged = False
			j = 0
			while j < len(lists) and not merged:
				if l[0] >= lists[j][0] and l[0] <= lists[j][1]:
					lists[j][1] = max(lists[j][1], l[1])
					merged = True
				if l[1] >= lists[j][0] and l[1] <= lists[j][1]:
					lists[j][0] = min(lists[j][0], l[0])
					merged = True
				j += 1
			if not merged:
				lists.append(l)
		old_n_list = n_list
		n_list = len(lists)
	acc = 0
	for l in lists:
		acc += l[1]-l[0]+1
	print(acc)


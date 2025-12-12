
filenames = ["input1.txt", "input2.txt"]



def no_paths(dic, from_="you", to_="out"):
	dic_dist = {}
	for key in dic.keys():
		if to_ in dic[key]:
			dic_dist[key] = 1

	old = ""
	tmp = str(dic_dist)
	while tmp != old:
		for key in dic.keys():
			ts = dic[key]
			all_found = True
			for k in ts:
				if not k in dic_dist.keys():
					all_found = False
			if all_found:
				dic_dist[key] = sum(dic_dist[k] for k in ts)
		old = tmp 
		tmp = str(dic_dist)
	return dic_dist[from_]


for filename in filenames[:]:
	dic = {}
	for line in open(filename):
		line = line.strip().split(" ")
		dic[line[0][:-1]] = line[1:]

	# part 1
	print(no_paths(dic, "you", "out"))
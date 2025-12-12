
filenames = ["input1.txt", "input2.txt", "input3.txt"]


def no_paths(dic, from_="you", to_="out"):
	dup = {}
	for key in dic.keys():
		dup[key] = dic[key]
	dic = dup
	dic[to_]=""
	del dic[to_]

	dic_dist = {}
	dic_dist[to_]=1
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


	old = ""
	tmp = str(dic_dist)

	while tmp != old:
		for key in dic.keys():
			#if not key in dic_dist.keys():
			acc = 0
			for k in dic[key]:
				if k in dic_dist.keys():
					acc += dic_dist[k]
			dic_dist[key] = acc
		dic_dist[to_]=1
		old = tmp 
		tmp = str(dic_dist)

	
	return dic_dist[from_]



# part 1
for filename in filenames[0:2]:
	dic = {}
	for line in open(filename):
		line = line.strip().split(" ")
		dic[line[0][:-1]] = line[1:]

	
	print(no_paths(dic, "you", "out"))


# part 2
for filename in filenames[2:0:-1]:
	dic = {}
	for line in open(filename):
		line = line.strip().split(" ")
		dic[line[0][:-1]] = line[1:]

	tmp1 = 1
	tmp1 *= no_paths(dic, "fft", "out")
	tmp1 *= no_paths(dic, "dac", "fft")
	tmp1 *= no_paths(dic, "svr", "dac")
	tmp2 = 1
	tmp2 *= no_paths(dic, "dac", "out")
	tmp2 *= no_paths(dic, "fft", "dac")
	tmp2 *= no_paths(dic, "svr", "fft")
	print(tmp1 + tmp2)


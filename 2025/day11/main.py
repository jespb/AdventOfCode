
filenames = ["input1.txt", "input2.txt", "input3.txt"]


def no_paths(dic, from_="you", to_="out"):
	cached = dic[to_] if to_ != "out" else None
	dic[to_]=""
	del dic[to_]

	dic_dist = {}
	dic_dist["out"]=0
	for key in dic.keys():
		dic_dist[key]=0
	dic_dist[to_]=1


	changed = True
	while changed:
		changed=False
		for key in dic.keys():
			acc = 0
			for k in dic[key]:
				acc += dic_dist[k]
			if dic_dist[key] != acc:
				changed=True
				dic_dist[key] = acc
		dic_dist[to_]=1

	if not cached is None:
		dic[to_] = cached
	return dic_dist[from_]


from time import time

# part 1
for filename in filenames[0:2]:
	time_s = time()
	dic = {}
	for line in open(filename):
		line = line.strip().split(" ")
		dic[line[0][:-1]] = line[1:]

	ans = no_paths(dic, "you", "out")
	print("%.4fs -- %d"%(time()-time_s, ans))


# part 2
for filename in filenames[2:0:-1]:
	time_s = time()
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
	print("%.4fs -- %d"%(time()-time_s, tmp1 + tmp2))


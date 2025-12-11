
filenames = ["input1.txt", "input2.txt"]

def filldic(dic, dic_dist, curr="you"):
	if curr in dic_dist.keys():
		return dic_dist[curr]
	else:
		acc = 0
		for k in dic[curr]:
			tmp = filldic(dic, dic_dist, k)
			dic_dist[k] = tmp
			acc += tmp

for filename in filenames[:1]:
	dic = {}
	for line in open(filename):
		line = line.strip().split(" ")
		dic[line[0][:-1]] = line[1:]
	print(dic)

	dic_dist = {}
	for key in dic.keys():
		if "out" in dic[key]:
			dic_dist[key] = 1

	print(dic_dist)
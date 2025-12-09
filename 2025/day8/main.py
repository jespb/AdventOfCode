
filenames = ["input1.txt", "input2.txt"]

def distance(p1,p2):
	if p1==p2:
		return 10**4
	return float("%.3f" % (((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5))

def closestPair(distmap):
	min_ , i1 = min(distmap[0]), 0
	i2 = distmap[i1].index(min_)
	for j in range(len(distmap)):
		if min(distmap[j])<min_:
			min_ = min(distmap[j])
			i1 = j 
			i2 = distmap[i1].index(min_)
	return min(i1, i2), max(i1, i2)



for filename in filenames[1:]:
	points = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]
	distmap = [[distance(p1,p2) for p2 in points] for p1 in points]
	circuits = [[i] for i in range(len(points))]


	connected = 0
	for _ in range(1000):
		print("\n---")
		shortest_dists = sorted([(min(distmap[i]),i) for i in range(len(distmap))])

		sd = shortest_dists[0]
		i1 = sd[1]
		i2 = distmap[i1].index(sd[0])

		circuits[i1].extend(circuits[i2])
		connected += 1
		print("connected %d and %d, with distance %f... we have a total of %d connections" % (i1,i2, distmap[i1][i2], connected))
		for ind in circuits[i1]:
			circuits[ind] = circuits[i1]

		#for ind1 in circuits[i1]:
		#	for ind2 in circuits[i1]:
		distmap[i1][i2] = 10**4
		distmap[i2][i1] = 10**4

		circuits = [ list(set(c)) for c in circuits]
		#print(circuits)

		#assert False

		circuits2 = [ str(list(set(c))) for c in circuits]
		circuits2 = list(set(circuits2))
		#print(circuits2)
		circuits2 = sorted([len(eval(c)) for c in circuits2])

		#print(circuits2)
		print(circuits2[-1]*circuits2[-2]*circuits2[-3])



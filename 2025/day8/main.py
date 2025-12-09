
filenames = ["input1.txt", "input2.txt"]

def distance(p1,p2):
	if p1==p2:
		return 10**10
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




def part1(filename):
	points = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]
	distmap = [[distance(p1,p2) for p2 in points] for p1 in points]
	circuits = [[i] for i in range(len(points))]

	for _ in range(1000):
		shortest_dists = sorted([(min(distmap[i]),i) for i in range(len(distmap))])

		sd = shortest_dists[0]
		i1 = sd[1]
		i2 = distmap[i1].index(sd[0])

		circuits[i1].extend(circuits[i2])

		for ind in circuits[i1]:
			circuits[ind] = circuits[i1]

		distmap[i1][i2] = 10**4
		distmap[i2][i1] = 10**4

		circuits = [ list(set(c)) for c in circuits]

	circuits2 = [ str(list(set(c))) for c in circuits]
	circuits2 = list(set(circuits2))
	circuits2 = sorted([len(eval(c)) for c in circuits2])

	if len(circuits2)>2:
		print(circuits2[-1]*circuits2[-2]*circuits2[-3])




def part2(filename):

	points = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]
	distmap = [[distance(p1,p2) for p2 in points] for p1 in points]
	circuits = [[i] for i in range(len(points))]


	no_circuits = len(circuits)
	while no_circuits > 1:
		shortest_dists = sorted([(min(distmap[i]),i) for i in range(len(distmap))])

		sd = shortest_dists[0]
		i1 = sd[1]
		i2 = distmap[i1].index(sd[0])

		circuits[i1].extend(circuits[i2])
		circuits[i1] = sorted(list(set(circuits[i1])))

		for ind in circuits[i1]:
			circuits[ind] = circuits[i1]

		for ind1 in circuits[i1]:
			for ind2 in circuits[i1]:
				distmap[ind1][ind2] = 10**10
				distmap[ind2][ind1] = 10**10


		circuits2 = [ str(c) for c in circuits]
		circuits2 = list(set(circuits2))

		#print(circuits2)
		no_circuits = len(circuits2)
		if no_circuits == 1:
			print(points[i1][0] * points[i2][0])





from time import time

for filename in filenames[1:]:
	ts = time()
	part1(filename)
	print("Part 1 time: %.3f(s)" %(time()-ts))

	ts = time()
	part2(filename)
	print("Part 2 time: %.3f(s)" %(time()-ts))






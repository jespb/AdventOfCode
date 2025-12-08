
filenames = ["input1.txt", "input2.txt"]

def distance(p1,p2):
	if p1==p2:
		return 10**10
	return float("%.1f" % (((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5))

for filename in filenames[:1]:
	points = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]
	distmap = [[distance(p1,p2) for p2 in points] for p1 in points]
	circuits = [[i] for i in range(len(points))]

	[print(l) for l in distmap]

	minlen = min([len(circuit) for circuit in circuits])
	while minlen==1:

		i1 = distmap.index(min(distmap))
		i2 = distmap[i1].index(min(distmap[i1]))
		
		circuits[i1].extend(circuits[i2])
		circuits[i2].extend(circuits[i1])

		for j1 in circuits[i1]:
			for k1 in circuits[i1]:
				distmap[j1][k1] = 10**10

		for j1 in circuits[i2]:
			for k1 in circuits[i2]:
				distmap[j1][k1] = 10**10

		minlen = min([len(circuit) for circuit in circuits])


		circuits = [ list(set(c)) for c in circuits]
		print(circuits, "\n---")

		#assert False

	circuits = [ list(set(c)) for c in circuits]
	print(circuits)
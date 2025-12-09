
filenames = ["input1.txt", "input2.txt"]


# part 1
for filename in filenames:

	m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

	pwd = []
	for p1 in m:
		pwd.append( [ (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)  for p2 in m] )

	ma = 0
	for line in pwd:
		ma =max(ma, max(line))

	print(ma)



# part 2
for filename in filenames:

	m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

	pwd = []
	for p1 in m:
		pwd.append( [ (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)  for p2 in m] )

	ma = 0
	for line in pwd:
		ma =max(ma, max(line))

	print(ma)

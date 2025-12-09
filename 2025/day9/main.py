
filenames = ["input1.txt", "input2.txt"]


# part 1
for filename in filenames[2:]:

	m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

	pwd = []
	for p1 in m:
		pwd.append( [ (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)  for p2 in m] )

	ma = 0
	for line in pwd:
		ma =max(ma, max(line))

	print(ma)



# part 2
def allowed(points, x,y):
	valid = [0,0,0,0]
	for py, px in points:
		if py>=y and px>=x:
			valid[0] = 1
		if py>=y and px<=x:
			valid[1] = 1
		if py<=y and px>=x:
			valid[2] = 1
		if py<=y and px<=x:
			valid[3] = 1
		if sum(valid) == 4:
			return True
	return False

for filename in filenames[1:]:

	m = [ [int(x) for x in line.strip().split(",")] for line in open(filename)]

	#tmp = [[0]*13 for _ in range(13)]
	#for y in range(13):
	#	for x in range(13):
	#		tmp[y][x] = "#" if allowed(m, y, x) else " "
	#for line in tmp:
	#	print(line)


	pwd = []
	for p1 in range(len(m)):
		print(p1/len(m))
		p1 = m[p1]
		tmp = [] 
		for p2 in m:
			valid = True
			yii, yia = min(p1[1], p2[1]), max(p1[1], p2[1])
			xii, xia = min(p1[0], p2[0]), max(p1[0], p2[0])
			yi = yii
			while valid and yi < yia:
				valid &= allowed(m, yi, xii)
				valid &= allowed(m, yi, xia)
				yi +=1
			xi = xii
			while valid and xi < xia:
				valid &= allowed(m, yii, xi)
				valid &= allowed(m, yia, xi)
				xi +=1
			if valid:
				tmp.append( (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1))
			else:
				tmp.append(0)
		pwd.append(tmp)

	ma = 0
	for line in pwd:
		ma =max(ma, max(line))

	print(ma)

# 1506688 too low

# 4638696212 too high
# 2116295688 too high
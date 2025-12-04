
filenames = ["input1.txt", "input2.txt"]

def openMap(filename):
	f = [s.strip() for s in open(filename) ]
	mapa1=[]
	mapa2=[]
	mapa3=[]
	mapa1.append(list("."*(len(f[0])+2)))
	mapa2.append(list("0"*(len(f[0])+2)))
	mapa3.append([0]*(len(f[0])+2))
	for line in f:
		mapa1.append(list(".%s."%line))
		mapa2.append(list("0"*(len(f[0])+2)))
		mapa3.append([0]*(len(f[0])+2))
	mapa1.append(list("."*(len(f[0])+2)))
	mapa2.append(list("0"*(len(f[0])+2)))
	mapa3.append([0]*(len(f[0])+2))
	return mapa1, mapa2, mapa3

def countNeighbours(mapa, y,x):
	acc = -1 #self
	for yi in range(y-1, y+2):
		for xi in range(x-1, x+2):
			if mapa[yi][xi] == "@":
				acc += 1
	return acc



for filename in filenames[:]:
	mapa, explored, reachable = openMap(filename)

	toExplore = [ (0,0) ]
	while len(toExplore)!=0:
		y,x = toExplore.pop()
		explored[y][x] = "1"
		if mapa[y][x] == "@":
			n = countNeighbours(mapa, y, x)
			if n < 4:
				reachable[y][x]=1
				mapa[y][x]="."
		#else: # empty space
		if y > 0 and explored[y-1][x]=="0":
			toExplore.append((y-1, x))
		if x > 0 and explored[y][x-1]=="0":
			toExplore.append((y, x-1))
		if y < len(mapa)-1 and explored[y+1][x]=="0":
			toExplore.append((y+1, x))
		if x < len(mapa[0])-1 and explored[y][x+1]=="0":
			toExplore.append((y, x+1))

	count = sum([sum(l) for l in reachable])
	
	print(count)


	mapa, explored, reachable = openMap(filename)

	lastcount = 0
	count = -1
	while lastcount != count:
		explored = [ ["0" for x in line] for line in explored]
		toExplore = [ (0,0) ]
		while len(toExplore)!=0:
			y,x = toExplore.pop()
			explored[y][x] = "1"
			if mapa[y][x] == "@":
				n = countNeighbours(mapa, y, x)
				if n < 4:
					reachable[y][x]=1
					mapa[y][x]="."
			#else: # empty space
			if y > 0 and explored[y-1][x]=="0":
				toExplore.append((y-1, x))
			if x > 0 and explored[y][x-1]=="0":
				toExplore.append((y, x-1))
			if y < len(mapa)-1 and explored[y+1][x]=="0":
				toExplore.append((y+1, x))
			if x < len(mapa[0])-1 and explored[y][x+1]=="0":
				toExplore.append((y, x+1))
		lastcount = count 
		count = sum([sum(l) for l in reachable])
	
	print(count)



	
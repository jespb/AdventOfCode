
filenames = ["input1.txt", "input2.txt"]

for f in filenames:
	# Part 1
	f = open(f).readline().strip().split(",")
	acc = 0
	for rang in f:
		rang = [int(x) for x in rang.split("-")]
		for n in range(rang[0], rang[1]+1):
			st = str(n)
			if len(st)%2 == 0:
				div = 1 + 10**(len(st)//2)
				if n/div == n//div:
					acc += n 
	print(acc)

	# Part 2
	def isValid(s):
		valid = True
		for step in range(1,len(s)//2+1):
			split = []
			for i in range(0,len(s),step):
				split.append(s[i: i+step])
			if len(list(set(split))) == 1:
				valid = False
		return valid


	acc = 0
	for rang in f:
		rang = [int(x) for x in rang.split("-")]
		for n in range(rang[0], rang[1]+1):
			s = str(n)
			if not isValid(s):
				acc += n 
	print(acc)


#4174379265
#33986149340
from time import time
from math import log10

filenames = ["input1.txt", "input2.txt"]

for f in filenames:
	print("\n>>>", f)
	# Part 1 v1
	t1 = time()
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
	t2 = time()
	print("Answer Pt1 v1: %20s -- Time(s): %.5f" % (acc, t2-t1)) 

	if False:
		# Part 2 v1
		t1 = time()
		def isValid(s):
			valid = True
			for step in range(1,len(s)//2+1):
				split = []
				for i in range(0,len(s),step):
					split.append(s[i: i+step])
				if len(list(set(split))) == 1:
					valid = False
					#print(s)
			return valid


		acc = 0
		for rang in f:
			rang = [int(x) for x in rang.split("-")]
			for n in range(rang[0], rang[1]+1):
				s = str(n)
				if not isValid(s):
					acc += n 
		t2 = time()
		print("Answer Pt2 v1: %20s -- Time(s): %.5f" % (acc, t2-t1)) # 54446379122


	# Part 2 v2
	t1 = time()
	def isValid(n):
		valid = True
		l = 1
		l_ = int(log10(n)+1)
		while l < l_ and valid:
			if l_%l==0:
				mul = 10**l
				e = n% mul
				n_ = n// mul 
				allSame = True
				while n_ != 0 and allSame:
					allSame = e == ( n_% mul )
					n_ = n_//mul

				if allSame:
					return False
			l += 1
		return valid

	acc = 0
	for rang in f:
		rang = [int(x) for x in rang.split("-")]
		for n in range(rang[0], rang[1]+1):
			if not isValid(n):
				acc += n 
	t2 = time()
	print("Answer Pt2 v2: %20s -- Time(s): %.5f" % (acc, t2-t1))


#4174379265
#33986149340


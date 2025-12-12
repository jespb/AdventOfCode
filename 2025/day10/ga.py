
i_ = [
[0,0,0,1],
[0,1,0,1],
[0,0,1,0],
[0,0,1,1],
[1,0,1,0],
[1,1,0,0],
]

o_ = [3,5,4,7]


from random import randint
p = [[0]*len(i_)]
for g in range(100):
	np = []
	# evaluation
	pev = []
	for ind in p:
		acc = [0]*len(o_)
		for wi in range(len(ind)):
			for indi in range(len(o_)):
				acc[indi] += i_[wi][indi]*ind[wi]
		fit = (sum([abs(acc[i]-o_[i]) for i in range(len(acc))]), sum(ind))
		#print(acc, o_, fit, ind)
		pev.append([fit, ind])

	pev.sort()

	print(pev[0])
	#[print(p) for p in pev]
	p = [ind[1] for ind in pev]


	# breeding
	for _ in range(100):
		s = p[ min(randint(0, len(p)-1), randint(0, len(p)-1) ) ][:]
		for z in range(len(s)):
			s[ z ] += randint(-1,1)
		s = [ max(i,0) for i in s]
		np.append(s)



	p = np


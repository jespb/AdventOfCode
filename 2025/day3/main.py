from time import time

filenames = ["input1.txt", "input2.txt"]


def searchForBatteryN(banks, n):
	acc = 0
	for bank in banks:
		bank = [int(x) for x in bank.strip()]
		bank_acc = 0
		index = 0
		for i in range(n-1,-1,-1):
			digit = max(bank[:-i] if i!=0 else bank)
			index = bank.index(digit)
			bank_acc += digit*(10**i)
			bank = bank[index+1:]
		acc +=  bank_acc
	return acc

for f in filenames[:]:

	# Part 1
	ts = time()
	n = 2
	banks = open(f)
	ans =searchForBatteryN(banks, n)
	te = time()
	print("Execution time for %s part 1: %.4fs -- Answer: %d" % (f, te-ts, ans) )

	# Part 2
	ts = time()
	n = 12
	banks = open(f)
	ans = searchForBatteryN(banks, n)
	te = time()
	print("Execution time for %s part 2: %.4fs -- Answer: %d" % (f, te-ts, ans) )

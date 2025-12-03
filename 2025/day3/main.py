
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
	print(acc)

for f in filenames[:]:

	# Part 1
	n = 2
	banks = open(f)
	searchForBatteryN(banks, n)

	# Part 2
	n = 12
	banks = open(f)
	searchForBatteryN(banks, n)

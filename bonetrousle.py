
t = int(input().strip())

for q in range(t):

	n,k,b = [int(x) for x in input().strip().split()]

	# n = number of sticks to buy
	# k = boxes available for purchase
	# b = boxes to buy

	# (x+1) + (x+2) + (x+3)...(x+b)
	# b*x + b*(b+1)/2 = n

	temp = n - ((b * (b + 1)) // 2)
	if temp % b == 0:
		temp = temp // b
	else:
		temp = (temp // b) + 1 # round up if necessary
	# we want to take the boxes x+1, x+2, x+3, ... x+b. But we might
	# have some left over.

	overbuy = (temp * b) + (((b) * (b + 1)) // 2) - n;
	answers = [int(x) for x in range(b)]
	for a in range(b):
		answers[a] = temp + a + 1
	
	for a in range(1, b + 1):
		if overbuy > 0:
			if overbuy > answers[a - 1] - a:
				overbuy -= answers[a - 1] - a
				answers[a - 1] = a
			else:
				answers[a - 1] -= overbuy
				overbuy = 0
	
	sum1 = 0
	OK = True;
	for  a in range(b):
		sum1 += answers[a]
		if answers[a] <= 0:
			OK = False
		if answers[a] > k:
			OK = False
	
	if sum1 != n:
		OK = False
	if not OK:
		print("-1");
	else:
		for a in range(b):
			if a != b - 1:
				print(answers[a], end=' ')
			else:
				print(answers[a], end='')
		print("\n", end='')

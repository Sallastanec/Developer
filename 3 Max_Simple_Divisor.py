def factorise(x):
	a = []
	divisor = 2
	while x>1:
		if x%divisor == 0:
			a.append (divisor)
			x //= divisor
		else:
			divisor += 1		 
	print (a[-1])
factorise (600851475143)
#First option:
summ = 0
summa_numbers = 0
for i in range(1000):
	if i%3==0 or i%5==0:
		summa_numbers +=i
print(summa_numbers)

#Second option:
b=[m for m in range(1000) if m%3==0 or m%5==0]
print(sum(b))
listfib = [1, 2]
while listfib [-1] < 4000000:
	listfib.append (listfib[-2] + listfib[-1])
	chet_fib = list(filter(lambda x: not x%2, listfib))
summfib=sum(chet_fib)
print(summfib)

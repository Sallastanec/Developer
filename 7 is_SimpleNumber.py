#Решаем через решето Эратосфена
b = [] 
N=105000
a = [True] * N
a[0] = a[1] = False
for k in range(2,N):
	if a[k]:
		for m in range (2*k, N, k):
			a[m] = False

for k in range (N):
	if a[k]:
		b.append(k)
print ((b[10001]))


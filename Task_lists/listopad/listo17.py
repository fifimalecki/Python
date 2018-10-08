lista = []

def Collatz(n):
	lista.append(int(n))
	if n == 1:
		print(lista)
		return 1
	elif n % 2 == 0:
		return Collatz(n / 2)
	elif n % 2 == 1:
		return Collatz(3 * n + 1)


Collatz(11)

from math import sqrt

A = int(input("Wprowadz wspolczynnik A= "))
B = int(input("Wprowadz wspolczynnik B= "))
C = int(input("Wprowadz wspolczynnik C= "))


def delta(a,b,c):
	return b**2 - 4*a*c

def solve(a,b,c):
	
	dsqrt = sqrt(delta(a,b,c))
	
	if a != 0:
		if delta(a,b,c) > 0:
			return (-b + dsqrt) / 2 / a, (-b - dsqrt) / 2 / a
		elif delta(a,b,c) == 0:
			return  -b / 2 / a
	else:
		print("To nie trojmian. ")

print(solve(A,B,C))

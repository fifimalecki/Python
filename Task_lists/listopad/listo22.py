import sys
import math

boki = []
if len(sys.argv[1:]) == 3:
	for arg in sys.argv[1:]:
		boki += arg
else:
	print("Zła liczba argumentów")
	sys.exit(0)

a = int(boki[0])
b = int(boki[1])
c = int(boki[2])

def obwod(boki):
	wynik = 0
	for bok in boki:
		wynik += int(bok)
	return wynik

print("Obwód =",obwod(boki))

def pole(a,b,c):
	return math.sqrt(((a+b+c)*(a+b)*(a+c)*(b+c))/16)

print("Pole =",pole(a,b,c))

def jakBoczny(a,b,c):
	if a == b and a == c and b == c:
		return "Trójkąt równoboczny"
	elif a == b or a == c or b == c:
		return "Trójkąt równoramienny"
	elif a != b and a != c and b != c:
		return "Trójkąt różnoboczny"

print(jakBoczny(a,b,c))

# Przerobione funkcje z listy pazdziernikowej z zadania 23
def max(a,b):
	if a > b:
		return a
	else:
		return b
def max2(*args):
	temp = args[0]
	for x in args[1:]:
		if max(temp,x) == x:
			temp = x
	return temp

def jakKatny(a,b,c):
	najwiekszy = max2(a,b,c)
	boki.remove(str(najwiekszy))
	A = int(boki[0])
	B = int(boki[1])
	if najwiekszy**2 == A**2 + B**2:
		return "Trójkąt prostokątny"
	elif najwiekszy**2 > A**2 + B**2:
		return "Trójkąt rozwartokątny"
	elif najwiekszy**2 < A**2 + B**2:
		return "Trójkąt ostrokątny"


print(jakKatny(a,b,c))
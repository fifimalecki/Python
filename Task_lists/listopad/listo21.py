import random
import os

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

def dzielniki(n):
	listaDzielnikow = []
	temp = n
	for i in range(1,n+1):
		if n%i == 0:
			listaDzielnikow.append(i)
			temp /= i
	return listaDzielnikow
cls()
while True:
	print("##################")
	print("# KURS MATEMTYKI #")
	print("##################")
	print("1. Dodawanie")
	print("2. Odejmowanie")
	print("3. Mnożenie")
	print("4. Dzielenie")
	print("5. Wyjście\n")

	option = int(input("Wybierz działanie: "))

	a = random.randint(0,100)
	b = random.randint(0,100)

	if option == 1:
		wynik = int(input(str(a)+"+"+str(b)+"="))
		if wynik == a + b:
			print("Dobrze")
		else:
			print("Źle")
	if option == 2:
		wynik = int(input(str(a)+"-"+str(b)+"="))
		if wynik == a - b:
			print("Dobrze")
		else:
			print("Źle")
	if option == 3:
		wynik = int(input(str(a)+"*"+str(b)+"="))
		if wynik == a * b:
			print("Dobrze")
		else:
			print("Źle")
	if option == 4:
		b = random.choice(dzielniki(a))
		wynik = int(input(str(a)+"/"+str(b)+"="))
		if wynik == a / b:
				print("Dobrze")
		else:
			print("Źle")
	if option == 5:
		break
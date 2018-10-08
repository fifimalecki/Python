import random

n = random.randint(0,100)
licznik = 0

while True:
	odp = int(input("?: "))
	roznica = odp - n
	licznik += 1
	if roznica > 50:
		print("duzo mniej")
	elif roznica > 10:
		print("mniej")
	elif roznica > 0:
		print("trochu mniej")
	elif roznica < 0:
		print("trochu wincyj")
	elif roznica < -10:
		print("wincyj")
	elif roznica < -50:
		print("duzo wincyj")
	elif n == odp:
		break
print("Liczba prob: ",str(licznik))
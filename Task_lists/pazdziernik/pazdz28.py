import math

def wczytaj_srednice():
    diameter = input("srednica= ")
    while True:
        try:
            diameter = float(diameter)
            break
        except:
            print("toż to nie liczba")
            diameter = input("= ")
    return diameter

R = wczytaj_srednice() / 2

def oblicz_obwod(R):
	return 2 * math.pi * R

def oblicz_pole(R):
	return math.pi * R**2

print("Pole = {:f}\nObwod = {:f}".format(oblicz_pole(R),oblicz_obwod(R)))
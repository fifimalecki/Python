import math

wybor = int(input("1. Kartezjanskie -> Sferyczne\n2. Sferyczne -> Kartezjanskie\n-> "))


def sfer2kart(r,theta,phi):
	#return (x,y,z)
	return r*math.sin(theta)*math.cos(phi),r*math.sin(theta)*math.sin(phi),r*math.cos(theta)

def kart2sfer(x,y,z):
	#return (r,theta,phi)
	return 	math.sqrt(x**2+y**2+z**2),(math.atan(math.sqrt(x**2+y**2)/z))**-1,(math.atan(y/x))**-1

def input():
	if wybor == 1:
		X = 1.1#float(input("Podaj x= "))
		Y = 1.2#float(input("Podaj y= "))
		Z = 1.3#float(input("Podaj z= "))
		return kart2sfer(X,Y,Z)
	elif wybor == 2:
		R = 1.1#float(input("Podaj r= "))
		T = 1.2#float(input("Podaj theta= "))
		P = 1.3#float(input("Podaj phi= "))
		if R >= 0.0 and P >= 0.0 and P < 2*math.pi() and T >= 0.0 and T <= math.pi():
			return sfer2kart(R,T,P)
		else:
			print("error")			

print(input())
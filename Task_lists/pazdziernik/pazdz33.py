import math

v_p = float(input("podaj v poczatkowe= "))
phi = float(input("podaj kat rzutu= "))
g = 9.8
t = 1

def czas(v_p,phi):
	return 2*v_p*math.sin(phi)/g

def h_max(v_p,phi):
	return (v_p*math.sin(phi))**2/2*g

def zasieg(v_p,phi):
	return v_p**2*math.sin(2*phi)/g

def polozenie(v_p,phi,t):
	return v_p*t*math.cos(phi), v_p*t*math.sin(phi)-g*t**2/2

print(czas(v_p,phi))
print(h_max(v_p,phi))
print(zasieg(v_p,phi))

while t != 0:
	t = float(input("podaj t= "))
	print(polozenie(v_p,phi,t))
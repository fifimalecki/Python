import math

def odleglosc(x1,y1,x2,y2):
	return ((x2-x1)**2 + (y2-y1)**2)**0.5

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

print(odleglosc(x1,y1,x2,y2))
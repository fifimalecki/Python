def dzielniki(n):
	listaDzielnikow = []
	temp = n
	for i in range(1,n+1):
		if n%i == 0:
			listaDzielnikow.append(i)
			temp /= i
	return listaDzielnikow

def generuj_slownik(n):
	newDict = {}
	for i in range(n+1):
		newDict[i] = dzielniki(i)
	return newDict

n = int(input("Podej n: "))

print(generuj_slownik(n))
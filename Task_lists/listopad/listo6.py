n = int(input("Podaj n: "))

# sito eratostenesa
def PrimeNumbers(n):
	tempList = list(range(2,n+1,1))
	for i in tempList:
		for j in range(0,n+1,1):
			if i**2+j*i in tempList:
				tempList.remove(i**2+j*i)

	return tempList

print(PrimeNumbers(n))
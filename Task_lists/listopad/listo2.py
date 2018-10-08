string = input("Podej= ")

numbers = list(range(0,10))

numbersFromInput = []

def MakeListOfNumbersFromInput(string):
	for i in string:
		if i in str(numbers):
			numbersFromInput.append(i)

def permutacja(tekst, indeks):
    if indeks < len_tekst:
        for i in range(indeks, len_tekst):
            tekst[i], tekst[indeks]  =  tekst[indeks], tekst[i]
            permutacja(tekst, i+1)
            tekst[i], tekst[indeks]  =  tekst[indeks], tekst[i]
    else: print(''.join(tekst))

MakeListOfNumbersFromInput(string)

len_tekst = len(numbersFromInput)
tekst = numbersFromInput

permutacja(tekst,0)
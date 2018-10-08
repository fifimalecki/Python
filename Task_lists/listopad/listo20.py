liczba = input("Podej binarna liczbe ziomek: ")
binary = "10"

def Bin2Dec(n):
	reverseN = n[::-1]
	temp = 0
	count = 0
	for char in n:
		if char not in binary:
			return "Dane są nieprawidłowe"
	else:
		for i in reverseN:
			temp += int(i)*(2**count)
			count += 1
	return temp

print(Bin2Dec(liczba))	
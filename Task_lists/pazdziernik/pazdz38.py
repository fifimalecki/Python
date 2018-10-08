zdanie = "kobyla ma maly bok"#input("Wprowadz zdanie = ")


def make_list(lista):
	temp = list()
	for x in lista:
		if x not in [" ",".",","]:
			temp.append(x)
	return temp

def palindrom(zdanie):
	temp = make_list(zdanie)

	for x in range(len(temp)):
		if temp[x] != temp[-x-1]:
			return "nie palindrom"
	return "palindrom"
			

print(palindrom(zdanie))

lista = [1,2,"dupd","kupk",3,4]


def foo(lista):
	temp = 0
	tempList = []
	for element in lista:
		if type(element) is str:
			tempList.append(element)
	for element in tempList:
		if element[-1:] == element[:1]:
			temp+=1
	return temp

print(foo(lista))
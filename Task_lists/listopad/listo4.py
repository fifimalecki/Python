lista1 = [1,2,3,4,5]
lista2 = [1,6,7,8,9]


def foo(lista1,lista2):
	for element1 in lista1:
		for element2 in lista2:
			if element1 == element2:
				return True
			else: return False

print(foo(lista1,lista2))
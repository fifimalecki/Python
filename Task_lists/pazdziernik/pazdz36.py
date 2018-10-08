import string

lista = string.ascii_lowercase

example = "The quick brown fox jumps over the lazy dog. False, I see false, this exam I may pass."
example2 = "przyklad"

def make_list(lista):
	temp = list()
	for x in lista:
		temp.append(x)
	return temp

lista2_0 = make_list(lista)

def check(string):
	temp = 0
	for x in string:	
		if x in lista2_0:
			temp = lista2_0.index(x)
			del(lista2_0[temp])
	return lista2_0

def result(string):
	if len(check(string)) == 0:
		print("Pangram=\n",string)
	else:
		print("Nie pangram=\n",string)

result(example2)
result(example)
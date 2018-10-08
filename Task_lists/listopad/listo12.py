dictonary = {"Klucz 1": 1, "Klucz 2": 2, "Klucz_3": 3}

def foo(dictonary):
	newDict = {}
	for key, value in dictonary.items():
		index = 0
		newKey = ""
		new = list(key)
		for letter in new:
			if letter == " ":
				new[index] = "_"
			else:
				index += 1
		newKey = "".join(new)
		newDict[newKey] = value
	return newDict

print(foo(dictonary))
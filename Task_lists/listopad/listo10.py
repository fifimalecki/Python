lista_zakupow = {}

def AddProduct(lista_zakupow):
	while True:
		product = input("Podaj produkt: ")
		if product == "":
			break
		price = int(input("Podaj cene: "))
		lista_zakupow[product] = price

def TheMostExpensive(lista_zakupow):
	theMostExpesiveProduct = []
	maxPrice = 0
	index = 0
	for product, price in lista_zakupow.items():
		if price > maxPrice:
			maxPrice = price
			if len(theMostExpesiveProduct) == 0:
				theMostExpesiveProduct.append(product)
			else:
				theMostExpesiveProduct.pop(index)
				theMostExpesiveProduct.append(product)
		elif price == maxPrice:
			theMostExpesiveProduct.append(product)
			index += 1
	return theMostExpesiveProduct

def Print(lista_zakupow):
	total = 0
	for product, price in lista_zakupow.items():
		total += price
		print(product, " ", price,"zł")
	print("Całkowity koszt: ",total,"zł")
	print("Najdroższy szajs: ", TheMostExpensive(lista_zakupow))


AddProduct(lista_zakupow)
Print(lista_zakupow)
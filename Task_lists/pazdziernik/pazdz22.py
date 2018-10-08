products = {"Chleb": 3.99, "Maslo": 6.59, "Szynka": 7.89, "Ser": 5.50, "Ketchup": 4.00}

for product, price in products.items():
	print(product, price)

print(sum(products.values())/len(products))

new_product = input("Nowy produkt: ")
new_price = input("Cena nowego produktu: ")

products[new_product] = float(new_price)

print(sum(products.values())/len(products))

def srednia(slownik):
	print(sum(slownik.values())/len(slownik))

del products["Szynka"]

srednia(products)
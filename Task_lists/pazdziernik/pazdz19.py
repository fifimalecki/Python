grocery = ['jajka','mleko','chleb','maslo','piwo']
n_items = []
prohibited = ['wodka','piwo','wino']

for product in grocery:
	n = input("Produkt " + product +": sztuk = ")
	if product in prohibited:
		n_items.append(0)
	else:
		n_items.append(n)

print("{:-^50}".format("Lista zakupow"), end="\n\n")

for i in range(len(grocery)):
	print(str(i+1),grocery[i],":",n_items[i])
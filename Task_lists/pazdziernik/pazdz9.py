krotka=(0,1,2,3,4,"pięć","sześć","siedem","osiem","dziewięć")
print(krotka[:3])
print(krotka[-2:])
print(krotka[::2][1:])
print(len(krotka))
print(len(krotka[-2]))
x=krotka
print(x[:5]+(5,6)+x[-3:])
print(x[:5],(5,6),x[-3:])
#nie mozna dodac bo jest immutable, a append nie 
#istnieje dla tuple
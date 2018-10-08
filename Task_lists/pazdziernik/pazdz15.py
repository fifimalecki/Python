help(id)

x = 2
y = x
print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))

x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))
#poniewaz zmienia sie adres pamieci. Przy zmianie w
#liscie adres pozostaje ten sam.
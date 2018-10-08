lista=list(range(3,100,3))
print(lista)
del lista[::3]
print(lista)
print(sum(lista)/len(lista))
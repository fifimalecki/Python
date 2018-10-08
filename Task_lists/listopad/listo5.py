from  itertools import combinations

stuff = [1, 2, 3]

def foo(LISTA):
	tempList = []
	for L in range(0, len(stuff)+1):
  		for subset in combinations(stuff, L):
  			tempList.append(list(subset))
  	
	return tempList

print(foo(stuff))
    
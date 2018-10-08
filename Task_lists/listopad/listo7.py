x = {'a':1 , 'b':2}
y = {'c':3 , 'd':4}

def MergeTwoDicts(x, y):
	z = x.copy()
	z.update(y)
	return z

print(MergeTwoDicts(x,y))
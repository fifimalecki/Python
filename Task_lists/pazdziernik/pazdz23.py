def min2_0(a,b):

	if a < b:
		return a
	else:
		return b

def min2_1(*args):

	temp = args[0]
	
	for x in args[1:]:
		if min2_0(temp,x) == x:
			temp = x

	return temp

print(min2_1(564,412,431,423,534,354))
a = int(input("a= "))
b = int(input("b= "))

def MultiplyNaturalNumbers(a,b):
	temp = 0
	for i in range(1,b+1,1):
		temp += a
	return temp


print(MultiplyNaturalNumbers(a))
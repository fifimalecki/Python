import cmath

def rozklad(x):
	if x <= 0:
		return 0
	i = 2
	temp = []
	
	while x != 1:
		if x % i == 0:
			temp.append(i)
			x /= i
			i = 2
		else:
			i += 1

	return temp

def NWD(a,b):
	temp1 = rozklad(a)
	temp2 = rozklad(b)

	temp_result = []
	result = 1

	if len(temp1) < len(temp2):
		for x in temp1:
			if x in temp2:
				temp_result.append(x)
				temp2.remove(x)

	elif len(temp2) < len(temp1):
		for x in temp2:
			if x in temp1:
				temp_result.append(x)
				temp1.remove(x)

	for x in temp_result:
		result *= x

	return result
				

def NWW(a,b):
	return int(a*b/NWD(a,b))
				
print(rozklad(1234))
print(NWD(8,8))
print(NWW(192,348))
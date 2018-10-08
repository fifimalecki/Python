from grudz5b import MaxHappyKids

def loadSet():
	temp = []
	tempS = []
	tempL = []
	S = []
	L = []
	control = False
	file = open("data.txt",'r')
	for char in file:
		temp += char
	for char in temp:
		if control == False:
			if char.isdigit() == True:
				tempS.append(int(char))
			elif char == ";":
				S.append(tempS)
				tempS=[]
				control = True
		elif control == True:
			if char.isdigit() == True:
				tempL.append(int(char))
			elif char == "\n":
				L.append(tempL)
				tempL=[]
				control = False
	return S,L

S,L = loadSet()

for i in range(0,len(S)):
	print("Liczba zadowolonych dzieci",MaxHappyKids(S[i],L[i]))
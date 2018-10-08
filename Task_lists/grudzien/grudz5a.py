import random
import sys

def RollSet(M=random.randint(1,10),N=random.randint(1,10)):
	S = []
	for s in range(0,M):
		S.append(random.randint(1,10))
	L = []
	for l in range(0,N):
		L.append(random.randint(1,10))
	#print(S,L)
	return S,L

def UpdateListOfSets(list1,list2,path):
	file = open(path,'a')
	for s in list1:
		if list1.index(s) == len(list1)-1:
			file.write(str(s))
		else:
			file.write(str(s)+", ")
	file.write("; ")
	for l in list2:
		if list2.index(l) == len(list2)-1:
			file.write(str(l))
		else:
			file.write(str(l)+", ")
	file.write("\n")

def main():
	for i in range(0,int(sys.argv[1])):
		S,L = RollSet()
		UpdateListOfSets(S,L,sys.argv[2])


main()
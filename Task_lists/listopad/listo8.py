import math

numbers = input("Podaj ciag liczb: ")

def MakeDict(numbers):
	tempList = numbers.split(" ")
	tempDict = {}
	for element in tempList:
		tempDict[element] = int(element)**2
	return tempDict

dictionary = MakeDict(numbers)	

def PrintDict(dictionary):
	for element1, element2 in dictionary.items():
		print(element1, "->", element2) 

print(PrintDict(dictionary))
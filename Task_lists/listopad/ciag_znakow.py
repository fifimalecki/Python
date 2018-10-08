import random
import string

def compress(string):
	if string.isalpha == False:
		return None
	newString = ""
	count = 0
	tempString = string[0] + str(count)
	for letter in string:
		if letter in tempString:
			count += 1
			tempString = letter + str(count)
		elif letter not in tempString:
			newString += tempString
			count = 1
			tempString = letter + str(count)
	newString += tempString
	newString = newString.replace("1","")

	return newString

def decompress(string):
	newString = ""
	temp = ""
	for letter in string:
		if letter.isalpha() == True:
			temp = letter
			newString += temp
		elif letter.isnumeric() == True:
			for i in range(int(letter)-1):
				newString += temp
	return newString

def test(n):
	tempString = ""
	tempChar = ""
	for i in range(random.randint(1,9)):
		tempChar = random.choice(string.ascii_letters)
		for j in range(random.randint(1,9)):
			tempString += tempChar
	compressedString = compress(tempString)
	decompressedString = decompress(compressedString)
	if( tempString == decompressedString):
		return True
	else:
		return False
import sys

importedFile = []
columns = int(sys.argv[1])
rows = int(sys.argv[2])

file = open(sys.argv[3],"r")
for letter in file:
	importedFile += letter
file.close()

words = []
tempWord = ""
freeColumns = columns
for letter in importedFile:
	if letter != " ":
		tempWord += letter
		if importedFile.index(letter) == (len(importedFile)-1):
			words.append(tempWord+" ")	
	else:
		words.append(tempWord+" ")
		tempWord = ""
result = ""
tempRows = rows-1
count = 0
while tempRows > 0:
	count += 1
	for word in words:
		if freeColumns >= len(word):
			result += word
			freeColumns -= len(word)
		elif tempRows <= 0:
			count -= 1
			break
		else:
			result = result[:-1]
			freeColumns += 1
			for i in range(0,freeColumns):
				result += "*"
				freeColumns -= 1
			if tempRows > 0:
				result += ("\n" + word)	
				tempRows -= 1
				freeColumns = columns - len(word)
result = result[:-1]
freeColumns += 1
for i in range(0,freeColumns):
				result += "*"

print("\n"+result)
print("\nWynik = ", count)
import sys
mode = 0
text = []

def ReadFile():
	line = []
	if sys.argv[1].isdigit() == False:
		file = open(sys.argv[1],'r')
		if len(sys.argv[2:]) == 0:
			mode = 0
		else:
			mode = int(sys.argv[2])
		for char in file:
			text.append(char)
		file.close
		return mode
	else:
		print("Nie ma argumentu obowiązkowego (plik do odczytu)")
		sys.exit(0)

mode = ReadFile()

def PrintFile(mode):
	if mode == 0:
		for char in text:
			print(char)
	if mode == 1:
		for char in text:
			if char[0] != '#':
				print(char)
	if mode == 2:
		for line in range(0,len(text)):
			text[line] = str(line+1) + ". " + text[line]
			print(text[line])

PrintFile(mode)
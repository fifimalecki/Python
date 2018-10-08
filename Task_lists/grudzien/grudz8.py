import os
import random
#0	- puste pole
#1 	- X
#2	- O
field = [[0 for x in range(3)] for y in range(3)]

#show cell value
def SCV(row,column):
	if field[row][column] == 0:
		return " "
	elif field[row][column] == 1:
		return "X"
	elif field[row][column] == 2:
		return "O"

def Clear():
	os.system('cls')#windows	
	#os.system('clear')#linux

def ShowGame():
	print("  1   2   3")
	print("A "+SCV(0,0)+" | "+SCV(0,1)+" | "+SCV(0,2))
	print("------------")
	print("B "+SCV(1,0)+" | "+SCV(1,1)+" | "+SCV(1,2))
	print("------------")
	print("C "+SCV(2,0)+" | "+SCV(2,1)+" | "+SCV(2,2))

def ChangeValue(row,column,value):
	if field[row][column] == 0:
		field[row][column] = value
		return True
	else:
		return False

def ChooseField():
	#zamiana liter na cyfry
	while True:
		print("Wybierz pole (LITERAcyfra)")
		tempChoose = input("Wybór= ")
		choose = list(tempChoose)
		if choose[0] == 'A':
			choose[0] = 0
			break
		elif choose[0] == 'B':
			choose[0] = 1
			break
		elif choose[0] == 'C':
			choose[0] = 2
			break

	return choose[0], int(choose[1])-1

def Win():
	somebodyWin = False
	#poziomo
	for i in range(0,3):
		if SCV(i,0) == SCV(i,1) == SCV(i,2):
			if (SCV(i,0) and SCV(i,1) and SCV(i,2)) == "X":
				print("Wygrywa X")
				somebodyWin = True
			elif (SCV(i,0) and SCV(i,1) and SCV(i,2)) == "O":
				print("Wygrywa O")
				somebodyWin = True
	#pionowo
	for i in range(0,3):
		if SCV(0,i) == SCV(1,i) == SCV(2,i):
			if (SCV(0,i) and SCV(1,i) and SCV(2,i)) == "X":
				print("Wygrywa X")
				somebodyWin = True
			elif (SCV(0,i) and SCV(1,i) and SCV(2,i)) == "O":
				print("Wygrywa O")
				somebodyWin = True
	#po skosach
	if SCV(0,0) == SCV(1,1) == SCV(2,2):
		if (SCV(0,0) and SCV(1,1) and SCV(2,2)) == "X":
			print("Wygrywa X")
			somebodyWin = True
		elif (SCV(0,0) and SCV(1,1) and SCV(2,2)) == "O":
			print("Wygrywa O")
			somebodyWin = True
	if SCV(0,2) == SCV(1,1) == SCV(2,0):
		if (SCV(0,2) and SCV(1,1) and SCV(2,0)) == "X":
			print("Wygrywa X")
			somebodyWin = True
		elif (SCV(0,2) and SCV(1,1) and SCV(2,0)) == "O":
			print("Wygrywa O")
			somebodyWin = True
	return somebodyWin

while True:
	player = random.randint(1,2)
	count = 0
	while True:
		Clear()
		ShowGame()
		if Win() == True:
			break
		else:
			if player == 1:
				print("Teraz X")
			elif player == 2:
				print("Teraz O")
		r,c=ChooseField()
		if ChangeValue(r,c,player) == True:
			if player == 1:
				player = 2
			elif player == 2:
				player = 1
			count += 1
			if count == 9:
				print("Remis")
				break
	break
	

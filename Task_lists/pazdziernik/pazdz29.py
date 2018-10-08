
samogloskiL = ["a","e","u","i","o","y"]
samogloskiU = [x.upper() for x in samogloskiL]
samogloski = samogloskiU + samogloskiL

def input_litera():

	temp = str(input("-> "))

	for x in temp:
		if x in samogloski:
			return 1
		else:
			continue
	return 0

def co(arg):
	
	if arg == 1:
		print("samogloska")
	else:
		print("nie ma samogloski")

co(input_litera())

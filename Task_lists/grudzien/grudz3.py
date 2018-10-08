filePython = open("studenci_python.txt","r")
listOfPythonStudents = []
for char in filePython:
	if '\n' in char:
		listOfPythonStudents.append(char[:-1])
	else:
		listOfPythonStudents.append(char)
filePython.close()

fileCpp = open("studenci_cpp.txt","r")
listOfCppStudents = []
for char in fileCpp:
	if '\n' in char:
		listOfCppStudents.append(char[:-1])
	else:
		listOfCppStudents.append(char)
fileCpp.close()

#print(listOfPythonStudents)
#print(listOfCppStudents)
print(set(listOfPythonStudents) & set(listOfCppStudents))
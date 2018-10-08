dziennik = {"Matematyka": 4, "Fizyka": 5, "Informatyka": 3}

def Add2SubjectsAndGrades(dziennik):
	for i in range(2):
		subject = input("Podaj przedmiot: ")
		grade = input("Podaj ocene: ")
		dziennik[subject] = grade

def PrintListOfSubjects(dziennik):
	sumOfGrades = 0;
	count = 0;
	avarage = 0;
	for subject, grade in dziennik.items():
		print(subject, "->", grade)
	for grade in dziennik.values():
		sumOfGrades += int(grade)
		count +=1
	avarage = sumOfGrades / count
	print("Średnia ocen",avarage)

Add2SubjectsAndGrades(dziennik)
PrintListOfSubjects(dziennik)
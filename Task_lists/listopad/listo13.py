import random

imiona = ("Kasia","Basia","Marek","Darek")
nazwiska = ("Nowak","Burak","Smith","Doe")
przedmioty = ("Matematyka","Fizyka","Chemia")

def generuj_studenta():
	"""Funkcja zwraca losowe imię i nazwisko"""
	return "{} {}".format(random.choice(imiona), random.choice(nazwiska))

def generuj_dziennik(n):
	"""Funkcja generuje n studentów i przypisuje im lsoowe oceny"""
	studenci = []

	for i in range(n):
		# dodaje losowo wygenerowego studenta z unikalnym id
		student = {
			"id": i,
			"student": generuj_studenta()
		}

		# generuje losowe oceny
		for przedmiot in przedmioty:
			student[przedmiot] = random.randint(2,5)

		# dodaj studenta z ocenami do dziennika

		studenci.append(student)

	return studenci

students = generuj_dziennik(5)

def drukuj_dziennik(studenci):
	"""Drukuje listę studentów wraz z ocenami"""
	for student in studenci:
		print("{}. {}".format(student["id"] + 1, student["student"]))

		for przedmiot in przedmioty:
			print("\t- {}: {}".format(przedmiot, student[przedmiot]))

def zmien_oceny_na_srednia(studenci):
	for student in studenci:
		count = 0
		sumOfGrades = 0
		for przedmiot in przedmioty:
			sumOfGrades += student[przedmiot]
			count += 1
			del student[przedmiot]
		student["Średnia"] = sumOfGrades/count
	return studenci
	

print(zmien_oceny_na_srednia(students))
# print(students)

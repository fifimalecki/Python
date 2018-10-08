import string
import random

lista = string.ascii_letters + string.digits

def generate_password(n):
	password = ""
	for i in range(n):
		password += lista[random.randrange(0,len(lista),1)]

	return password

print(generate_password(30))
from collections import Counter

string = input("Podej= ")

def Check(string):
	for val in Counter(string).values():
		if val > 1:
			return "nie zawiera unikatowych znakow"
	return "zawiera unikatowe znaki"

print(Check(string))
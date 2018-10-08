import random

def RollSet(M=random.randint(1,10),N=random.randint(1,10)):
	S = []
	for s in range(0,M):
		S.append(random.randint(1,10))
	L = []
	for l in range(0,N):
		L.append(random.randint(1,10))
	return L,S

def MaxHappyKids(CookiesList,kidsList):
	kids = kidsList
	kids.sort()
	cookies = CookiesList
	cookies.sort()
	maxKid = max(kidsList)
	maxCookie = max(CookiesList)
	happyKids = 0
	lenKids = len(kids)
	print("Dzieci:\n", kids,"\nCiastka:\n",cookies)
	while lenKids >= 0:
		#print(kids,"\t",cookies,"\t",happyKids,maxKid)
		tempListForMaxKid = [i for i in cookies if i >= maxKid]

		#print("temp=",tempListForMaxKid)
		if maxKid in tempListForMaxKid:
			tempMaxKid = max(tempListForMaxKid)
			cookies.remove(tempMaxKid)
			if maxKid in kids:
				kids.remove(maxKid)
				if lenKids > 1:
					maxKid = max(kids)
				elif lenKids == 2:
				 	print("KIDS",kids)
			else:
				break
			happyKids += 1
		else:
			if maxKid in kids:
				kids.remove(maxKid)
				if lenKids > 1:
					maxKid = max(kids)
				# else:
				# 	print(kids)
			else:
				break
		lenKids -= 1
	return happyKids

#print(MaxHappyKids(S,L))

def main():
	for i in range(1,random.randint(2,10)):
		L,S = RollSet()
		print("Liczba zadowolonych dzieci",MaxHappyKids(L,S))
main()
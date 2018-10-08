def foo(*args, **args1):

	for x in args:
		print(args.index(x)+1,"->",x)

	for key, value in args1.items():
		print(args1)

slownik = {"przyklad": 1}

foo(1,2,3,4,slownik)


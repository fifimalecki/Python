import turtle

length = eval(input("Podaj dlugosc boku: "))
N = eval(input("Podaj ilosc kwadratow: "))

n_sides = 4

turtle.speed(20)
for i in range(N):
	turtle.right(360/N)
	for i in range(n_sides):
		turtle.forward(length)
		turtle.right(90)

turtle.mainloop()
def horner(x, *arg):
    result = 0
    for wsp in reversed(arg):
        result = result * x + wsp
    return result

x = 1.0
wsp = [6,5,-13,1,1]

print(horner(x,*wsp))
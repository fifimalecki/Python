import ciag_znakow

string = "AAABBBBCAAAaaDD"
string2 = "A3B4CA3a2D2"

print(ciag_znakow.compress(string))

print(ciag_znakow.decompress(string2))

print(ciag_znakow.test(5))
key = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
key2_0 = {"a": "t","b": "w","c": "4","d": "4","e": "x","f": "m","g": "u","h": "r","i": "g","j": "7","k": "2","l": "d","m": "z","n": "pl","o": "bu","p": "g5","q": "h","r": "b4","s": "v","t": "y","u": "s","v": "tt","w": "g","x": "m","y": "5","z": "n",}

def _change_key(key):

	temp = {}

	for k,v in key.items():
		temp[v] = k

	return temp

def _crypt(key):

	_PHRASE = input("Podaj tekst do szyfrowania.\nTekst=")	
	temp = list()

	for x in _PHRASE:
		if x in  key.values():
			x = key[x]
			temp.append(x)
		else:
			temp.append(x)

	return ''.join(temp)

def _decrypt(key, phrase):

	temp = list()

	for x in phrase:
		if x in key.keys():
			x = key[x]
			temp.append(x)
		else:
			temp.append(x)

	return ''.join(temp)

decrypt_key = _change_key(key)
decrypt_key2 = {v: k for k, v in key.items()}

print(_crypt(key))
print(_decrypt(decrypt_key, "noi zypamnoj a dakumintycjo"))
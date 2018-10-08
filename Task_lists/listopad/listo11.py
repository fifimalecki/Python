dictionary = { "a": 1, "b": 1, "c": 2}

def RemoveIfSameValue(dictionary):
	newDict = {}
	for key, value in dictionary.items():
   		if value not in newDict.values():
   			newDict[key] = value
	return newDict

RemoveIfSameValue(dictionary)
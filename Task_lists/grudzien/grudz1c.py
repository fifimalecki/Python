from temperature_convert import Celcius2Fahrenheit
from temperature_convert import Fahrenheit2Celcius
from grudz1b import OpenCelciusFile
import math

def OpenFahrenheitFile():
	ListOfTemperature=[]
	tempListOfTemperature=[]
	tempTemperature=[]
	file = open("fahrenheit.txt",'r')
	for letter in file:
			tempListOfTemperature += letter
	for temperature in tempListOfTemperature:
		if '\n' not in temperature:
			tempTemperature += temperature
		else:
			CorrectTemperature = ''.join(tempTemperature)
			ListOfTemperature.append(float(CorrectTemperature))
			tempTemperature=[]
	return ListOfTemperature

def test():
	ListOfFahrenheits = OpenFahrenheitFile()
	ListOfCelciuses = OpenCelciusFile()
	ListOfConvertetFahrenheits = []
	ListOfConvertetCelciuses = []
	for temperature in ListOfFahrenheits:
		ListOfConvertetFahrenheits.append(Fahrenheit2Celcius(temperature))
	for temperature in ListOfCelciuses:
		ListOfConvertetCelciuses.append(Celcius2Fahrenheit(temperature))
	for i in range(0,len(ListOfFahrenheits)):
		if ListOfFahrenheits[i] != ListOfConvertetCelciuses[i]:
			print(False,ListOfFahrenheits[i],ListOfConvertetCelciuses[i])
	for i in range(0,len(ListOfCelciuses)):
		if ListOfCelciuses[i] != ListOfConvertetFahrenheits[i]:
			print(False,ListOfCelciuses[i],ListOfConvertetFahrenheits[i])
	# print(ListOfFahrenheits)
	# print(ListOfCelciuses)
	# print(ListOfConvertetFahrenheits)
	# print(ListOfConvertetCelciuses)
test()
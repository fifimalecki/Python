from temperature_convert import *

from temperature_convert import Celcius2Fahrenheit

def OpenCelciusFile():
	ListOfTemperature=[]
	tempListOfTemperature=[]
	tempTemperature=[]
	file = open("celcjusz.txt",'r')
	for letter in file:
			tempListOfTemperature += letter
	for temperature in tempListOfTemperature:
		if '\n' not in temperature:
			tempTemperature += temperature
		else:
			CorrectTemperature = ''.join(tempTemperature)
			ListOfTemperature.append(int(CorrectTemperature))
			tempTemperature=[]
	return ListOfTemperature

def ConvertImporetedCelcius2Fahrenheit():
    ListOfTemperatureInCelcius = OpenCelciusFile()
    file = open("fahrenheit.txt",'w')
    for temperature in ListOfTemperatureInCelcius:
    	file.write(str(Celcius2Fahrenheit(temperature))+'\n')
    file.close

ConvertImporetedCelcius2Fahrenheit()
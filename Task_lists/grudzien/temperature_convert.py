import random
import math

def Celcius2Fahrenheit(temperature):
	return round((temperature*1.8) + 32,1)

def Fahrenheit2Celcius(temperature):
    return round((temperature-32)/1.8,1)

def RandomTemperature(N):
        ListOfTemperature=[]
        for i in range(0,N):
                ListOfTemperature.append(random.randint(0,100))

        return ListOfTemperature

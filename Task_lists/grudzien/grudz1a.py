from temperature_convert import RandomTemperature
import sys

def GenerateRandomCelcius():
    file = open("celcjusz.txt","w")
    if sys.argv[1].isdigit() is True:
   		for temperature in RandomTemperature(int(sys.argv[1])):
   			file.write(str(temperature)+"\n")
    else:
   		print("Argument nie jest typu int")
   		sys.exit(0)
    file.close

GenerateRandomCelcius()


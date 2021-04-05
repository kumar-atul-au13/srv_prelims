class Temprature:
    def __init__(self):
        pass

    def convertFahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    def convertCelsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius


celsius = input("Input celsius")
try:
    celsius = float(celsius)
    if 0 > celsius or celsius > 100:
        print("Enter valid celsius range")
    else:
        farn=Temprature.convertFahrenheit(celsius)
        print(farn)
except ValueError:
    print("Invalid celsius input")

fahrenheit = input("Input farenheit")
try:
    fahrenheit = float(fahrenheit)
    if fahrenheit <32 or fahrenheit>212:
        print("Enter valid Fahrenhit range")
    else:
        cels=Temprature.convertCelsius(fahrenheit)
        print(cels)
except ValueError:
    print("Invalid fahrenheit input")

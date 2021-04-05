import math


class Circle:
    def __init__(self, radius):
        try:
            if float(radius) :
                self.radius = float(radius)
        except ValueError:
            print("Invalid Input")

    def getarea(self):
        return math.pi * self.radius * self.radius

    def getcircumference(self):
        return 2 * math.pi * self.radius


try:
    radius = float(input("Enter radius "))
    if radius > 0:
        circle = Circle(radius)
        print("area is", circle.getarea(), "perimeter is ", circle.getcircumference())
    else:
        print("Enter positive radius")
except ValueError:
    print("Enter valid input")

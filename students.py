class Student:
    def __init__(self, name="", roll=None):
        if name.isalpha() and str(roll).isdigit():
            self.name = name
            self.roll = roll
        else:
            self.name = None
            self.roll = None
            print("invalid name or roll")

    def display(self):
        print("name of the student is ", self.name, "roll of the student is ", self.roll)
        if self.age:
            print("age is ",self.age)
        if self.marks:
            print("marks is ", self.marks)

    def setAge(self,age):
        if str(age).isdigit():
            self.age=age
        else:
            self.age=None
            print("Invalid age")

    def setMarks(self,marks):
        if str(marks).isdigit() and marks <= 100:
            self.marks = 100
        else:
            self.marks = None
            print("invalid marks")




stu = Student("adf", 23)
stu.setAge(-34)
stu.setMarks(1000)
stu.display()

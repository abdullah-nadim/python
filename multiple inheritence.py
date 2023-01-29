class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Dancer:
    def __init__(self, style):
        self.style = style

class Student(Human,Dancer):
    def __init__(self,name, age,gender, style):
        Human.__init__(self,name,age,gender)
        Dancer.__init__(self,style)

John = Student("John",21,"Male","Hiphop")
print(John.age,John.name,John.gender,John.style)
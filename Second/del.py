class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
print(s1.name)
del s1.name
print(s1.name)  # This will raise an AttributeError since name has been deleted
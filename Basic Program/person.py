class Person:
    __name = "anonymous"  # private attribute

    def __hello(self):
        print("Hello, person!")

    def wellcome(self):
        self.__hello()

p1 = Person()
print(p1.wellcome())  # This will raise an AttributeError since __name is private
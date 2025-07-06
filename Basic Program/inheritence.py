class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotoCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotoCar("Corolla")
car2 = ToyotoCar("Camry")


print(car1.start())
print(car2.name)
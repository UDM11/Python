class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(5)
print("Area of circle with radius 5:", c1.area())
print("Circumference of circle with radius 5:", c1.circumference())
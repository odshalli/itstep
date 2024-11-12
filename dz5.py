class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print("Площа прямокутника:", rect.calculate_area())
print("Периметр прямокутника:", rect.calculate_perimeter())

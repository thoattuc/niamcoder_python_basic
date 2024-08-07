class Car:
    num_wheels = 4

    def __init__(self, color, style):
        self.color = color
        self.style = style
        self.speed = 0

    def change_speed(self, speed):
        self.speed = speed

    def change_color(self, color):
        self.color = color


my_car = Car(color="black", style="Sedan")
# your_car = Car("White", "Hatchback")
# her_car = Car("Red", style="SUV")
print(my_car.color)
my_car.color = "Orange"
print(my_car.style)

# del my_car.color
# print(my_car.color)     # AttributeError: 'Car' object has no attribute 'color'

# del my_car
# print(my_car)     # NameError: name 'my_car' is not defined

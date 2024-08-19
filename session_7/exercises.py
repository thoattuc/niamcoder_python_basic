class Car:
    num_wheels = 4

    def __init__(self, color, style):
        self.color = color
        self.style = style
        self.speed = 0

    def change_speed(self, new_speed):
        self.speed = new_speed

    def change_color(self, new_color):
        self.color = new_color


if __name__ == '__main__':
    my_car = Car(color="black", style="Sedan")
    # your_car = Car("White", "Hatchback")
    # her_car = Car("Red", style="SUV")
    print(my_car.color)
    print(my_car.style)
    print("--------------------------------")
    my_car.color = "Orange"
    print(my_car.color)
    print(my_car.style)


# del my_car.color
# print(my_car.color)     # AttributeError: 'Car' object has no attribute 'color'

# del my_car
# print(my_car)     # NameError: name 'my_car' is not defined

# Inheritance - Encapsulates - Polymorphism - Abstraction

# inheritance: class ChildClass(ParentClass):
# class FuelCar(Car):
#     pass

# Override a method
class FuelCar(Car):
    num_wheels = 4

    def __init__(self, color, style, fuel_type):
        super().__init__(color, style)
        self.fuel_type = fuel_type
        self.speed = 0


if __name__ == '__main__':
    my_car = FuelCar("while", "sport", "oil")
    print(my_car.color, my_car.style, my_car.fuel_type)
    my_car.change_speed(200)
    print(my_car.speed)


class ElectricCar(Car):
    pass

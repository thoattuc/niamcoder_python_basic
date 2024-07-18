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


class ElectricCar(Car):
    def __init__(self, color, style, fuel):
        super().__init__(color, style)
        self.fuel = fuel


my_car = Car(color="black", style="sport")


class BankAccount:
    def __init__(self, name, password, balance=0, bank_type="normal"):
        self.name = name
        self.password = password
        self.balance = balance
        self.type = bank_type

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Amount should be a positive number and cant be exceed balance")

    def deposit(self, amount):
        if 0 < amount:
            self.balance += amount


class VIPBankAccount(BankAccount):
    def __init__(self, name, password, balance):
        if balance >= 1e6:
            super().__init__(name, password, balance, bank_type="vip")
        else:
            super().__init__(name, password, balance, bank_type="normal")
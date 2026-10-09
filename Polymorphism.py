#Polymorphism : Vehicle Rental System

class Car:
    def calculate_rent(self, days):
        return days * 1000


class Bike:
    def calculate_rent(self, days):
        return days * 500


class Bus:
    def calculate_rent(self, days):
        return days * 2000


# Creating objects
car = Car()
bike = Bike()
bus = Bus()

days = 3

print("Car Rent:", car.calculate_rent(days))
print("Bike Rent:", bike.calculate_rent(days))
print("Bus Rent:", bus.calculate_rent(days))
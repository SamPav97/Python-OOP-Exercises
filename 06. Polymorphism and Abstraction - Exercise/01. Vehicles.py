from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, fuel):
        pass

    @abstractmethod
    def refuel(self, distance):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        ac_drive = self.fuel_consumption + 0.9
        distance_available = (self.fuel_quantity / ac_drive)
        if distance_available >= distance:
            subtract_fuel = distance * ac_drive
            self.fuel_quantity -= subtract_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        ac_drive = self.fuel_consumption + 1.6
        distance_available = (self.fuel_quantity / ac_drive)
        if distance_available >= distance:
            subtract_fuel = distance * ac_drive
            self.fuel_quantity -= subtract_fuel

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


car = Car(20, 5)
car.drive(5)
print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)

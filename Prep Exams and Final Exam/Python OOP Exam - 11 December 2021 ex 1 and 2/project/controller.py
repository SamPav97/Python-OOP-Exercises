from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def check_x_in_y(self, model):
        for x in self.cars:
            if x.model == model:
                return True
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type == "MuscleCar":
            x = MuscleCar(model, speed_limit)
            if self.check_x_in_y(model):
                raise Exception(f"Car {model} is already created!")
            self.cars.append(x)
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            x = SportsCar(model, speed_limit)
            if self.check_x_in_y(model):
                raise Exception(f"Car {model} is already created!")
            self.cars.append(x)
            return f"{car_type} {model} is created."
        else:
            pass

    def check_driver(self, name):
        for x in self.drivers:
            if x.name == name:
                return x
        return False

    def create_driver(self, driver_name: str):
        x = Driver(driver_name)
        if self.check_x_in_y(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(x)
        return f"Driver {driver_name} is created."

    def check_race(self, name):
        for x in self.races:
            if x.name == name:
                return x
        return False

    def create_race(self, race_name: str):
        x = Race(race_name)
        if self.check_race(race_name):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(x)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.check_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                shofer = self.check_driver(driver_name)
                if shofer.car:
                    z = shofer.car
                    shofer.car = car
                    car.is_taken = True
                    z.is_taken = False
                    return f"Driver {driver_name} changed his car from {z.model} to {car.model}."
                else:
                    shofer.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} chose the car {car.model}."
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.check_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        if not self.check_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        shofer = self.check_driver(driver_name)
        if not shofer.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        racce = self.check_race(race_name)
        for driver in racce.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."
        racce.drivers.append(shofer)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        res = ""
        if not self.check_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = self.check_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[0:3]
        for driver in winners:
            driver.number_of_wins += 1
            res += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
        return res.strip()


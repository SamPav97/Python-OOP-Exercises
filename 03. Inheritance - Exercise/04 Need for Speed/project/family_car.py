from project.car import Car


class FamilyCar(Car):

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)
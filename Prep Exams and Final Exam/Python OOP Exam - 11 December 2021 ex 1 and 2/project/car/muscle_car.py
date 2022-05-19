from project.car.car import Car


class MuscleCar(Car):
    MAX_SPEED_LIMIT = 450
    MIN_SPEED_LIMIT = 250

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)


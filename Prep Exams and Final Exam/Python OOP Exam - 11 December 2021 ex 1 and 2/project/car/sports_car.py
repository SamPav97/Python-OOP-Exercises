from project.car.car import Car


class SportsCar(Car):
    MAX_SPEED_LIMIT = 600
    MIN_SPEED_LIMIT = 400

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)


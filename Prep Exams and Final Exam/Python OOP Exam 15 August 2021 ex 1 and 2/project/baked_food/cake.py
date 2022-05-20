from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    #Will it understand that the 200 refers to portion?
    def __init__(self, name, price):
        super().__init__(name, 245, price)

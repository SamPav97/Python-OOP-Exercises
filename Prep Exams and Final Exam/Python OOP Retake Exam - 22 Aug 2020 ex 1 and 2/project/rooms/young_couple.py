from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, pension1, pension2):
        super().__init__(family_name, pension1 + pension2, 2)
        # not sure if this is how they want this attr
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]

    def calc_exp(self):
        x = self.calculate_expenses(self.appliances)
        return x + self.room_cost

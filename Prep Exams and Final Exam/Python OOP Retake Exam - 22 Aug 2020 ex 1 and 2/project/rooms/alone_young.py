from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, budget):
        super().__init__(family_name, budget, 1)
        # not sure if this is how they want this attr
        self.room_cost = 10
        self.appliances = [TV()]

    def calc_exp(self):
        x = self.calculate_expenses(self.appliances)
        return x + self.room_cost #Or maybe not * 30
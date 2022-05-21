from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension1, pension2):
        super().__init__(family_name, (pension1 + pension2), 2)
        # not sure if this is how they want this attr
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

##I CHANGED THE EXPENSES WHEREBY NOW IN THE ROOM IT RETURNS FOR ALL MEMBERS NOT HERE
    def calc_exp(self):
        x = self.calculate_expenses(self.appliances)
        return x + self.room_cost

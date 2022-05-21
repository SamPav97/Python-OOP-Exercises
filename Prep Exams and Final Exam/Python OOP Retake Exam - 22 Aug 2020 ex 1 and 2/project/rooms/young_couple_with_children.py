from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, pension1, pension2, *children):
        super().__init__(family_name, (pension1 + pension2), (2+len(children)))
        # is this how they want the children plus parents?
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count

    def calc_exp(self):
        self.calculate_expenses(self.appliances)
        x = self.expenses
        x += sum([x.cost for x in self.children]) * 30
        return x + self.room_cost

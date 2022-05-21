from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, budget):
        super().__init__(family_name, budget, 1)
        #not sure if this is how they want this attr
        self.room_cost = 10

    def calc_exp(self):
        return self.room_cost #Or maybe not * 30
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []
        #this may not work if the method for monthly cons wasnt called beforethat
        self.monthly_consumption = 0

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.calc_exp()
        self.monthly_consumption = total
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        res = ""
        for room in self.rooms:
            if room.budget >= room.calc_exp():
                room.budget -= room.calc_exp()
                res += f"{room.family_name} paid {room.calc_exp():.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                res += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return res.strip()

    def status(self):
        all_ppl = sum([x.members_count for x in self.rooms])
        res = f"Total population: {all_ppl}\n"
        for room in self.rooms:
            res += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.calc_exp()-room.room_cost:.2f}$\n"
            if room.__class__.__name__ == "YoungCoupleWithChildren":
                for ind, child in enumerate(room.children):
                    ind += 1
                    res += f"--- Child {ind} monthly cost: {child.cost * 30:.2f}$\n"
            if room.__class__.__name__ == "AloneOld":
                res += f"--- Appliances monthly cost: {0:.2f}$\n"
            else:
                res += f"--- Appliances monthly cost: {room.calculate_expenses(room.appliances):.2f}$\n"
        return res.strip()

# from unittest import TestCase
#
# class EverlandTest(TestCase):
#
#     def test_montly_cons(self):
#         hotel = Everland()
#         y = Child(20, 12, 7)
#         x = YoungCoupleWithChildren("Dobrovi", 1000, 2000, y)
#         hotel.add_room(x)
#         x = hotel.get_monthly_consumptions()
#         self.assertEqual(100, x)

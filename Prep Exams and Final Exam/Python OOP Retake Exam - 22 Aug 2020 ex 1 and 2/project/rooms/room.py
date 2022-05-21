from project.appliances.tv import TV


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = [] #contains objects of children
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        s = len(args)
        total = 0
        for arg in args:
            total += sum([x.cost for x in arg]) * 30
        self.expenses = total
        return total

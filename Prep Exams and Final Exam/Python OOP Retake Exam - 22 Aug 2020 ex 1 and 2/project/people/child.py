class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)
#
# kid = Child(3, 4, 6, 7)
# print(kid.cost)
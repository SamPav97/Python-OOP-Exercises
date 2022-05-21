from project.supply.supply import Supply


class Drink(Supply):

    def __init__(self, name):
        super().__init__(name, 15)  # It says 25 is an optional parameter. Not sure what that means.

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

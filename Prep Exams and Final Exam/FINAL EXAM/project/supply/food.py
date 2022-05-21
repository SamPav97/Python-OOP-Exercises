from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name, food=25):
        super().__init__(name, food) #It says 25 is an optional parameter. Not sure what that means.

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

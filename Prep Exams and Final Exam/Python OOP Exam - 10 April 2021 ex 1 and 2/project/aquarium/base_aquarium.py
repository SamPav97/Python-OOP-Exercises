from abc import ABC, abstractmethod


#possible class for mistakes
class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([x.comfort for x in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return "Water not suitable"

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        #I CHANGED THIS
        count = 0
        for fishy in self.fish:
            count += 1
            fishy.eat()
        return count

    def __str__(self):
        names = [x.name for x in self.fish]
        res = f"{self.name}:\n"
        if len(self.fish) > 0:
            res += f"Fish: {' '.join(names)}\n"
        else:
            res += f"Fish: none\n"
        res += f"Decorations: {len(self.decorations)}\n"
        res += f"Comfort: {self.calculate_comfort()}\n"
        return res


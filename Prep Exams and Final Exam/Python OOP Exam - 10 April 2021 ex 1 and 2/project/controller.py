from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        #here you might have to check if aquarium name already in aquariums
        if aquarium_type == "FreshwaterAquarium":
            x = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            x = SaltwaterAquarium(aquarium_name)
        else:
            return "Invalid aquarium type."
        self.aquariums.append(x)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            x = Ornament()
        elif decoration_type == "Plant":
            x = Plant()
        else:
            return "Invalid decoration type."
        self.decorations_repository.add(x)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium_names = [x.name for x in self.aquariums]
        if aquarium_name in aquarium_names:
            for deco in self.decorations_repository.decorations:
                if deco.__class__.__name__ == decoration_type:
                    for aquarium in self.aquariums:
                        if aquarium.name == aquarium_name:
                            aquarium.add_decoration(deco)
                            self.decorations_repository.remove(deco)
                            return f"Successfully added {decoration_type} to {aquarium_name}."
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                if fish_type == "FreshwaterFish" and aquarium.__class__.__name__ == "FreshwaterAquarium":
                    x = FreshwaterFish(fish_name, fish_species, price)
                    return aquarium.add_fish(x)
                elif fish_type == "SaltwaterFish" and aquarium.__class__.__name__ == "SaltwaterAquarium":
                    x = SaltwaterFish(fish_name, fish_species, price)
                    return aquarium.add_fish(x)
                else:
                    return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                s = aquarium.feed()
        return f"Fish fed: {s}"

    def calculate_value(self, aquarium_name: str):
        total = 0
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                x = [x.price for x in aquarium.fish]
                total += sum(x)
                y = [x.price for x in aquarium.decorations]
                total += sum(y)
                return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        res = ""
        for aquarium in self.aquariums:
            res += str(aquarium)
        return res.strip()


# from unittest import TestCase
#
# class ControllerTest(TestCase):
#
#     def test_repr(self):
#         control = Controller()
#         control.add_aquarium("SaltwaterAquarium", "solenovodko")
#         control.add_aquarium("SaltwaterAquarium", "Sladkovodko")
#         control.add_decoration("Plant")
#         control.add_decoration("Plant")
#         control.add_fish("solenovodko", "SaltwaterFish", "sami", "pastarva", 2.5)
#         control.add_fish("solenovodko", "SaltwaterFish", "niki", "pastarva", 2.5)
#         control.insert_decoration("solenovodko", "Plant")
#         control.insert_decoration("solenovodko", "Plant")
#         x = control.report()
#         self.assertEqual("Successfully added Plant to solenovodko.", x)
#
#     def test_add_fish(self):
#         control = Controller()
#         control.add_aquarium("SaltwaterAquarium", "solenovodko")
#         control.add_decoration("Plant")
#         control.insert_decoration("solenovodko", "Plant")
#         x = control.add_fish("solenovodko", "SaltwaterFish", "sami", "pastarva", 2.5)
#         self.assertEqual("Successfully added Plant to solenovodko.", x)
#
#     def test_insert_deco_happy_case(self):
#         control = Controller()
#         control.add_aquarium("SaltwaterAquarium", "solenovodko")
#         control.add_decoration("Plant")
#         x = control.insert_decoration("solenovodko", "Plant")
#         self.assertEqual("Successfully added Plant to solenovodko.", control.aquariums[0].decorations)
#
#     def test_insert_deco_returns(self):
#         control = Controller()
#         control.add_aquarium("SaltwaterAquarium", "solenovodko")
#         control.add_decoration("Plant")
#         x = control.insert_decoration("solenovodko", "kur")
#         self.assertEqual("Successfully added Plant to solenovodko.", x)
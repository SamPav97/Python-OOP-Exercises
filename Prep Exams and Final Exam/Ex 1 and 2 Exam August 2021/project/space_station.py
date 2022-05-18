from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.success = 0
        self.fail = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            x = Biologist(name)
        elif astronaut_type == "Geodesist":
            x = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            x = Meteorologist(name)
        self.astronaut_repository.astronauts.append(x)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        x = Planet(name)
        x.items = items.split(", ")
        self.planet_repository.planets.append(x)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.astronauts.remove(astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astr in self.astronaut_repository.astronauts:
            astr.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):

        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        possible_astros = []
        for astro in self.astronaut_repository.astronauts:
            if astro.oxygen > 30:
                possible_astros.append(astro)
        possible_astros.sort(key=lambda x: x.oxygen, reverse=True)
        possible_astros = possible_astros[0:5]

        if len(possible_astros) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        planet = self.planet_repository.find_by_name(planet_name)
        count = 0
        for astro in possible_astros:
            count += 1
            if len(planet.items) < 1:
                self.success += 1
                return f"Planet: {planet_name} was explored. {count} astronauts participated in collecting items."
            while astro.oxygen > 0:
                if len(planet.items) < 1:
                    self.success += 1
                    return f"Planet: {planet_name} was explored. {count} astronauts participated in collecting items."
                astro.backpack.append(planet.items.pop())
                astro.breathe()
        self.fail += 1
        return "Mission is not completed."

    def report(self):
        res = f"{self.success} successful missions!\n"
        res += f"{self.fail} missions were not completed!\n"
        res += "Astronauts' info:\n"
        for astr in self.astronaut_repository.astronauts:
            res += f"Name: {astr.name}\n"
            res += f"Oxygen: {astr.oxygen}\n"
            if len(astr.backpack) == 0:
                res += f"Backpack items: none\n"
            else:
                res += f"Backpack items: {', '.join(astr.backpack)}\n"
        return res.strip()



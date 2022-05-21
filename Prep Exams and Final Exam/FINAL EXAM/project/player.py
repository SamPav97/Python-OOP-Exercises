from project.controller import Controller


class Player:
    all_names = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name #TODO check for duplicates
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = False
        #TODO Does the above work? NOOOOOOO because they set it to 0 and it doesn't understand that it was set

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        if value in Player.all_names:
            raise Exception(f"Name {value} is already used!")
        #this doesnt seem to work. find a way to make sure already existing names are not created
        Player.all_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 <= value <= 100:
            if value == 100:
                self.__need_sustenance = False
            else:
                self.__need_sustenance = True
            self.__stamina = value
        else:
            raise ValueError("Stamina not valid!")

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.__need_sustenance}"

class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}"
        result += "\n" + f"Guild: {self.guild}"
        result += "\n" + f"HP: {self.hp}"
        result += "\n" + f"MP: {self.mp}"
        for skill, mana in self.skills.items():
            result += "\n" + f"==={skill} - {mana}"
        return result


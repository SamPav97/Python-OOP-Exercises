class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    # def __iter__(self):
    #     for x in self.players:
    #         yield x

    def add_player(self, *args):
        added = []
        for person in args:
            if person in self.players:
                continue
            # if self.check_player(person):
            #     raise Exception(f"Name {person.name} is already used!")
            #     #Really not sure if this should be here
            #     #Exception here means that it might add all the ppl up to the exception.
            #     # Do i want this or should I remove them? Also what do I do if there is people after the error.
            # else:

            self.players.append(person)
            added.append(person.name)

        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def return_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def return_supply_of_type(self, sust_type):
        for supply in reversed(self.supplies):
            if supply.__class__.__name__ == sust_type:
                to_be_returned = supply
                self.supplies.reverse()
                self.supplies.remove(supply)
                self.supplies.reverse()
                return to_be_returned
        return None

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.return_player(player_name)
        if player:
            if not player._Player__need_sustenance:
                return f"{player_name} have enough stamina."
            if player.stamina == 100:
                return f"{player_name} have enough stamina."
            else:
                supply = self.return_supply_of_type(sustenance_type)
                if sustenance_type == "Food" and not supply:
                    raise Exception("There are no food supplies left!")
                elif sustenance_type == "Drink" and not supply:
                    raise Exception("There are no drink supplies left!")
                if supply:
                    if player.stamina + supply.energy > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy
                    return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.return_player(first_player_name)
        player2 = self.return_player(second_player_name)
        if player1.stamina == 0 and player2.stamina == 0:
            res = f"Player {first_player_name} does not have enough stamina.\n"
            res += f"Player {second_player_name} does not have enough stamina."
            return res
        elif player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player1.stamina < player2.stamina:
            if player2.stamina - (player1.stamina / 2) < 0:
                player2.stamina = 0
                return f"Winner: {player1.name}"
            else:
                player2.stamina -= player1.stamina / 2

            if player1.stamina - (player2.stamina / 2) < 0:
                player1.stamina = 0
                return f"Winner: {player2.name}"
            else:
                player1.stamina -= player2.stamina / 2

            if player1.stamina > player2.stamina:
                return f"Winner: {player1.name}"
            else:
                return f"Winner: {player2.name}"

        elif player1.stamina > player2.stamina:
            if player1.stamina - (player2.stamina / 2) < 0:
                player1.stamina = 0
                return f"Winner: {player2.name}"
            else:
                player1.stamina -= player2.stamina / 2

            if player2.stamina - (player1.stamina / 2) < 0:
                player2.stamina = 0
                return f"Winner: {player1.name}"
            else:
                player2.stamina -= player1.stamina / 2

            if player2.stamina > player1.stamina:
                return f"Winner: {player2.name}"
            else:
                return f"Winner: {player1.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) <= 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        res = ""
        for player in self.players:
            res += str(player) + "\n"
        for supply in self.supplies:
            res += supply.details() + "\n"
        return res.strip()


#SOMETHING NOT RIGHT IN SUSTANANCE. FEEDS AND MAYBE DRINKS WRONG. I SHOULDNT HAVE 2 CHEESES RETURNED. 1 CHEESE. 1 APPLE

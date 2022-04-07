from pokemon import Bulbasaur, Charmander, Squirtle


class PokeTeam:
    limit = 6
    battle_mode = 0
    criterion = ""
    charm_list = []
    bulb_list = []
    squir_list = []
    team = []

    def __init__(self) -> None:
        limit = 6
        battle_mode = 0

    def choose_team(self, new_battle_mode, new_criterion):
        battle_mode = new_battle_mode
        criterion = new_criterion
        is_valid = False
        while not is_valid:
            choice = input(
                "Howdy Trainer! Choose your team as C B S\nwhere C is the number of Charmanders\nB is the number of Bulbasaurs\nS is the number of Squirtles\n"
            )
            x = choice.split()
            if len(x) == 3 and (x[0] + x[1] + x[2] <= self.limit):
                is_valid = True

        self.assign_team(x[0], x[1], x[2])

    def assign_team(self, charm, bulb, squir):
        for i in range(charm):
            temp_charm = Charmander()
            self.team.append(temp_charm)
        for i in range(bulb):
            temp_bulb = Bulbasaur()
            self.team.append(temp_bulb)
        for i in range(squir):
            temp_squir = Squirtle()
            self.team.append(temp_squir)

    def print(self):
        for pokemon in self.team:
            print(
                pokemon.get_name()
                + " 's HP = "
                + pokemon.get_hp()
                + " and level = "
                + pokemon.get_level()
            )
            print(",")

from pokemon import Bulbasaur, Charmander, Squirtle
from stack_adt import ArrayStack


class PokeTeam:
    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        self.LIMIT = 6
        self.battle_mode = 0
        self.criterion = None
        self.teamlist = []
        self.team = None

    # TODO: constrain battle mode to 0, 1, 2
    def choose_team(self, battle_mode, criterion):
        self.battle_mode = battle_mode
        self.criterion = criterion
        is_valid = False
        while not is_valid:
            choice = input(
                "Howdy Trainer! Choose your team as C B S\nwhere C is the number of Charmanders\nB is the number of Bulbasaurs\nS is the number of Squirtles\n"
            )
            x = list(map(int, choice.split()))
            if len(x) == 3 and (x[0] + x[1] + x[2] <= self.LIMIT):
                is_valid = True

        self.assign_team(x[0], x[1], x[2])

    def assign_team(self, charm, bulb, squir):

        # create the list of pokemon
        for i in range(charm):
            temp_charm = Charmander()
            self.teamlist.append(temp_charm)
        for i in range(bulb):
            temp_bulb = Bulbasaur()
            self.teamlist.append(temp_bulb)
        for i in range(squir):
            temp_squir = Squirtle()
            self.teamlist.append(temp_squir)

        # Battle mode 0 is the set battle type
        # it uses the stack ADT
        if self.battle_mode == 0:
            teamADT = ArrayStack(self.LIMIT)
            for pokemon in self.teamlist:
                teamADT.push(pokemon)
            self.team = teamADT

    def __str__(self):
        string = ""
        if self.battle_mode == 0:
            # stack prints bottom to top, so we reverse it
            for pokemon in list(reversed(self.team.view())):
                string += str(pokemon) + ", "
        return string[:-2]

from poke_team import PokeTeam
from pokemon_base import PokemonBase


class Battle:
    team1 = None
    team2 = None
    trainer1 = ""
    trainer2 = ""

    def __init__(self, trainer_one_name, trainer_two_name):
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)

        self.trainer1 = trainer_one_name
        self.trainer2 = trainer_two_name

    def battle_step(self, p1, p2):
        speed1 = p1.get_speed()
        speed2 = p2.get_speed()
        # p1 attacks p2, then swap
        if speed1 > speed2:
            p2.resolve_damage(p1.get_poketype(), p1.get_attackdamage())
            if not p2.is_fainted:
                p1.resolve_damage(p2.get_poketype(), p2.get_attackdamage())
        # p2 attacks p1, then swap
        elif speed2 > speed1:
            p1.resolve_damage(p2.get_poketype(), p2.get_attackdamage())
            if not p1.is_fainted:
                p2.resolve_damage(p1.get_poketype(), p1.get_attackdamage())
        # p1 and p2 attack/defend at the same time
        else:
            p1.resolve_damage(p2.get_poketype(), p2.get_attackdamage())
            p2.resolve_damage(p1.get_poketype(), p1.get_attackdamage())

    def faint_step(self, p1, p2, battle_mode):
        if p1.is_fainted():
            if battle_mode == 0:
                self.team1.team.pop()
            elif battle_mode == 1:
                self.team1.team.serve()

            if not p2.is_fainted():
                p2.level_up()

        if p2.is_fainted():
            if battle_mode == 0:
                self.team2.team.pop()
            elif battle_mode == 1:
                self.team2.team.serve()
            if not p1.is_fainted():
                p1.level_up()

        if not p1.is_fainted() and not p2.is_fainted():
            p1.damage(1)
            p2.damage(1)

            if p1.is_fainted():
                if battle_mode == 0:
                    self.team1.team.pop()
                elif battle_mode == 1:
                    self.team1.team.serve()
                if not p2.is_fainted():
                    p2.level_up()

            if p2.is_fainted():
                if battle_mode == 0:
                    self.team2.team.pop()
                elif battle_mode == 1:
                    self.team2.team.serve()
                if not p1.is_fainted():
                    p1.level_up()

    def win_step(self):
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            return "Draw"
        elif self.team1.team.is_empty():
            return self.trainer2
        else:
            return self.trainer1

    def set_mode_battle(self):
        self.team1.choose_team(battle_mode=0, criterion=None)
        self.team2.choose_team(battle_mode=0, criterion=None)

        while not (self.team1.team.is_empty() or self.team2.team.is_empty()):
            p1: PokemonBase = self.team1.team.peek()
            p2: PokemonBase = self.team2.team.peek()

            self.battle_step(p1, p2)
            self.faint_step(p1, p2, battle_mode=0)

        return self.win_step()

    def rotating_mode_battle(self):
        pass

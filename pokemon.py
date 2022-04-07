from curses import get_tabsize
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    def __init__(self):
        self.hp = 7
        self.poke_type = "Fire"
        self.level = 1

        self.base_attack = 7
        self.base_defence = 4
        self.base_speed = 7

    def get_name(self):
        return "Charmander"

    def get_attackdamage(self):
        return self.base_attack + self.level

    def get_defence(self):
        return self.base_defence

    def get_speed(self):
        return self.base_speed + self.level

    def get_poketype(self):
        return self.poke_type

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def get_type_effectiveness(self, attacking_type):
        return super().get_type_effectiveness(self, attacking_type)

    def resolve_damage(self, attacking_type, damage):
        damage = damage * self.get_type_effectiveness(attacking_type)

        if damage > self.get_defence():
            self.hp = self.hp - damage
        else:
            self.hp = self.hp - damage / 2


class Bulbasaur(PokemonBase):
    def __init__(self):
        self.hp = 9
        self.poke_type = "Grass"
        self.level = 1

        self.base_attack = 5
        self.base_defence = 5
        self.base_speed = 7

    def get_name(self):
        return "Bulbasaur"

    def get_attackdamage(self):
        return self.base_attack

    def get_defence(self):
        return self.base_defence

    def get_speed(self):
        return self.base_speed + self.level // 2

    def get_poketype(self):
        return self.poke_type

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def get_type_effectiveness(self, attacking_type):
        return super().get_type_effectiveness(self, attacking_type)

    def resolve_damage(self, attacking_type, damage):
        damage = damage * self.get_type_effectiveness(attacking_type)
        if damage > self.get_defence() + 5:
            self.hp = self.hp - damage
        else:
            self.hp = self.hp - damage // 2


class Squirtle(PokemonBase):
    def __init__(self):
        self.hp = 8
        self.poke_type = "Water"
        self.level = 1

        self.base_attack = 4
        self.base_defence = 6
        self.base_speed = 7

    def get_name(self):
        return "Squirtle"

    def get_attackdamage(self):
        return self.base_attack + self.level // 2

    def get_defence(self):
        return self.base_defence + 6

    def get_speed(self):
        return self.base_speed

    def get_poketype(self):
        return self.poke_type

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def get_type_effectiveness(self, attacking_type):
        return super().get_type_effectiveness(self, attacking_type)

    def resolve_damage(self, attacking_type, damage):
        damage = damage * self.get_type_effectiveness(attacking_type)
        if damage > self.get_defence() * 2:
            self.hp = self.hp - damage
        else:
            self.hp = self.hp - damage // 2

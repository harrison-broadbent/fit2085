from abc import ABC, abstractmethod


class PokemonBase(ABC):
    name = ""
    poke_type = ""
    hp = 0
    level = 0

    base_speed = 0
    base_attack = 0
    base_defence = 0

    @abstractmethod
    def __init__(self, hp, poke_type):
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    @abstractmethod
    def get_hp(self):
        return self.hp

    @abstractmethod
    def set_hp(self, new_hp):
        self.hp = new_hp

    @abstractmethod
    def get_level(self):
        return self.level

    @abstractmethod
    def set_level(self, new_level):
        self.level = new_level

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def get_speed(self):
        return self.base_speed

    @abstractmethod
    def get_attackdamage(self):
        return self.base_attack

    @abstractmethod
    def get_poketype(self):
        return self.poke_type

    @abstractmethod
    def resolve_damage(self, attacking_type, damage):
        return NotImplemented

    @abstractmethod
    def get_defence(self):
        return self.base_defence

    # get the damage multiplier when we get attacked
    @abstractmethod
    def get_type_effectiveness(self, attacking_type):
        if self.poke_type == "Fire":
            if attacking_type == "Fire":
                return 1
            elif attacking_type == "Water":
                return 2
            elif attacking_type == "Grass":
                return 0.5

        elif self.poke_type == "Water":
            if attacking_type == "Fire":
                return 0.5
            elif attacking_type == "Water":
                return 1
            elif attacking_type == "Grass":
                return 2

        elif self.poke_type == "Grass":
            if attacking_type == "Fire":
                return 2
            elif attacking_type == "Water":
                return 0.5
            elif attacking_type == "Grass":
                return 1

    def __str__(self):
        return self.name + " 's HP = " + self.hp + " and level = " + self.level

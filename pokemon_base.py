from abc import ABC, abstractmethod


class PokemonBase(ABC):
    def __init__(self, hp, poke_type):
        self.hp = hp
        self.level = 1
        self.poke_type = poke_type

    @abstractmethod
    def get_name(self):
        pass

    def is_fainted(self):
        return not (self.hp > 0)

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_level(self):
        return self.level

    def level_up(self):
        self.level += 1

    def damage(self, damage):
        self.hp -= damage

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_attackdamage(self):
        pass

    @abstractmethod
    def get_defence(self):
        pass

    def get_poketype(self):
        return self.poke_type

    @abstractmethod
    def resolve_damage(self, attacking_type, damage):
        pass

    # get the damage multiplier when we get attacked
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
        return (
            self.get_name()
            + "'s HP = "
            + str(self.hp)
            + " and level = "
            + str(self.level)
        )

import random

class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level
    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )
    def get_defensive_roll(self):
        return random.randint(1,12) * self.level

class Human(Creature):
    def __init__(self, name, level):
        # more class stuff!
        super().__init__(name, level)

    def attack(self, creature):
        print("The warrior {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The Hero has destroyed {}".format(creature.name))
            return True
        else:
            print("The Hero has fallen.")
            return False

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

class Dragon(Creature):
    def __init__(self, name, level, scale_def, breathes_fire):
        super().__init__(name, level)
        self.scale_def = scale_def
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        #fire_modifier = None
        #if self.breathes_fire:
        #    fire_modifier = 5
        #else
        #    fire_modifier = 1
        #fire_modifer = VALUE_IF_TRUE if SOME TEST else VALUE_IF_FALSE
        fire_modifer = 5 if self.breathes_fire else 1

        scale_modifier = self.scale_def / 10

        return base_roll * fire_modifer * scale_modifier
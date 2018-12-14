#import actors
import random
import time

from actors import Human, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()

def print_header():
    print('-----------------------')
    print('     SIMPLE RPG        ')
    print('-----------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Human('Dark Knight', 10)
    ]

    hero = Human('Kenji', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest....'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
               creatures.remove(active_creature)
            else:
                print("The Hero runs to go recover...")
                time.sleep(5)
                print("The Hero has returned!")
        elif cmd == 'r':
            print('The Hero escapes the battle!')
        elif cmd == 'l':
            print('The Hero {} takes in the surroundings and sees '.format(hero.name))
            for c  in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Quitting game...Farewell!')
            break


        if not creatures:
            print("You have won the game!")
            break
        print()


if __name__ == '__main__':
        main()
# use this import to use the random modules
# import random
import random

print('----------------------------------')
print('    Guess that number game')
print('----------------------------------')
print()




# this is the random module thing
#the_number = random.randint(0, 100)

the_number = random.randint(0, 100)

guess = -1
name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, Your guess of {} was too low'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, Your guess of {} was too high'.format(name, guess))
    else:
        print('Congratulations {}! The number was {}. You win!'.format(name, guess))

print('Done!')





#Returns string
#print(guess_text, type(guess_text))

#Returns int
#print(guess, type(guess))


#This doesn't work in python, it causes an error
#print(the_number < guess_text)


#print('Sorry, {1} , Your guess of {0} was too low'.format(guess, name))
#You can switch name and guess and not put any numbers to achieve the same effect as the top
#print('Sorry, {} , Your guess of {} was too low'.format(name, guess))

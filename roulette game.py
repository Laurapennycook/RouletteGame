import random
amount = input('How much do you want to bet? ')
colour_ = input('Which colour do you choose? red/black ')
number = input('Choose a number between 1 and 20 ')
number_win = amount * 2
combo_win = amount * 100

def colour():
    random_number = random.randint(1, 2)
    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'
    return colour
random_number = random.randint(1, 20)
random_colour = colour()
print('Your number is {} and your colour is {}.'.format(random_number, random_colour))

if colour_ == random_colour and number == random_number:
    print('You win 100 times the amount you bet, {}!!'.format(combo_win))
elif number == random_number and colour_ != random_colour:
    print('You win double the amount you bet, {}!'.format(number_win))
elif colour_ == random_colour and number != random_number:
    print('You keep the amount you bet, {}.'.format(amount))
else:
    print('You win 0.')

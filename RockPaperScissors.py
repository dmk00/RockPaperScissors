# This is my first try at coding a game with simple rules: Rock Paper Scissors.
# The rules are simple:
# Rock beats Scissors
# Paper beats Rock
# Scissors beat Paper
# Same choices result in a Draw

# The first version: 1 Person against 1 Computer

# The choices:

import inquirer
import random

items = ['Rock', 'Paper', 'Scissors']

print('This will be a simple sudden death Rock-Paper-Scissors.',
      '\nYou can choose from the following: \n\u2022 ' + items[0],
      '\n\u2022 ' + items[1],
      '\n\u2022 ' + items[2])

input('\nPress Enter to continue...\n')


def get_choices(answers):
    return list(items)


questions = [
    inquirer.List('choice',
                  message='Please select your choice for this round',
                  choices=get_choices,
                  )
]
answers = inquirer.prompt(questions)

player = answers['choice']
computer = random.choice(items)

print(player)
print(computer)

if player == computer:
    print('This is a Draw!')
elif player == 'Rock' and computer == 'Scissors' or player == 'Paper' and computer == 'Rock' or player == 'Scissors' and computer == 'Paper':
    print('The player wins.')
else:
    print('The computer wins.')

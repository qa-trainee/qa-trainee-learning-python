# ATBS_S5_L12.py is a proram that wrote to test my understanding of
# Automate the boring stuff Section 5, Lecture 12

# Guess the number game

import random

# Assigns a random integer between 1 and 20 to secretNumber
secretNumber = random.randint(1, 20)
print('Which number I am thinking of between 1 and 20?')

for i in range(1, 6):
    guess = int(input('Take a guess:\n'))
    if guess == secretNumber:
        print('Good Job, you guessed my number in ' + str(i) + ' guesses.')
        break
    elif guess > secretNumber:
        print('Thats high, ' + str(5-i) + ' guesses left.')
    elif guess < secretNumber:
            print('Thats low, ' + str(5-i) + ' guesses left.')

if guess != secretNumber:
    print('You ran out of chances, my number was ' + str(secretNumber))

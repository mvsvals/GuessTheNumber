import random

random_number = random.randint(1, 100)

while True:
    player_guess = input('Guess the number (1-100): ')
    if not player_guess.isdigit():
        print('Invalid Input. Try again...')
        continue
    player_guess = int(player_guess)
    if player_guess == random_number:
        print('You guessed it!')
        break
    elif player_guess > random_number:
        print('Too High!')
    else:
        print('Too Low!')
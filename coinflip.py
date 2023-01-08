# Project information: https://discuss.codecademy.com/t/computer-science-independent-project-1-coin-flip/419951?_gl=1*1hvpca4*_ga*NzE2MTE1NjM5Ny4xNjcyMzY3MDk3*_ga_3LRZM6TM9L*MTY3MjgyMzUyNC4xMC4xLjE2NzI4MzAzODguNjAuMC4w

# Basic requirements:
# As a user I want to be able to guess the outcome of a random coin flip(heads/tails)
# As a user I want to clearly see the result of the coin flip.
# As a user I want to clearly see whether or not I guessed correctly.

# Intermediate challenges:
# User Story: As a user I want to clearly see the updated guess history (correct count/total count).
# User Story: As a user I want to be able to quit the game or go again after each cycle.

# Advanced challenge:
# User Story: As a user I want to be able to guess the outcome of a 6-sided dice roll (1-6), with the same feature set as the coin flip (see above).

import random

def coin_flip():
    guess = guess_coin_side()
    answers = ["Heads", "Tails"]
    rand_flip = random.choice(answers)
    if (rand_flip == "Heads" and guess == "Tails") or (rand_flip == "Tails" and guess == "Heads"):
        print(guess + ", was the incorrect guess! Please try again.")
    else:
        print(guess + ", was the correct answer!")
    coin_flip()

def guess_coin_side():
    while True:
        guess = input("I flipped a coin, enter 'Heads' or 'Tails' to guess which side it landed on: \n")
        if isinstance(guess, str):
            guess = str(guess)
            if guess == "Heads" or guess == "Tails" or guess == "heads" or guess == "tails":
                break
            else:
                print("You must enter 'Heads' or 'Tails'. Try again.")
        else:
            print("You must enter 'Heads' or 'Tails'. Try again.")
    return str.capitalize(guess)

def main_menu():
    while True:
        choice = input("Welcome to this game. Please type the corresponding number to make a play choice:\n1. Coinflip\n2. View coinflip scores\n3. Play 'dice roll'\n4. View 'dice roll' scores\n")
        if choice.isdigit():
            choice = int(choice)
            break

def main():
    main_menu()

main()
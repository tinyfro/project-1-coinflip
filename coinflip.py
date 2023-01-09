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

dice_roll_score = []
coin_flip_score = []

def main():
    main_menu()

def main_menu():
    while True:
        choice = input("Welcome to the games menu. Please choose a number to make a choice:\n1. Play Coinflip\n2. View Coinflip scores\n3. Play Diceroll\n4. View Diceroll scores\n")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                coin_flip()
            elif choice == 2:
                pass
            elif choice == 3:
                dice_roll()
            elif choice == 4:
                pass
            else:
                print("To make a choice, please choose the corresponding number.")

def guess_coin_side():
    while True:
        guess = input("I flipped a coin, enter 'Heads' or 'Tails' to guess which side it landed on: ")
        if isinstance(guess, str):
            guess = str(guess)
            if guess == "Heads" or guess == "Tails" or guess == "heads" or guess == "tails":
                break
            else:
                print("You must enter 'Heads' or 'Tails'. Try again.")
        else:
            print("You must enter 'Heads' or 'Tails'. Try again.")
    return str.capitalize(guess)

def guess_dice_roll():
    while True:
        guess = input("I rolled a dice, enter the number that the dice rolled to: ")
        if guess.isdigit():
            guess = int(guess)
            if guess > 0 and guess <= 6:
                break
            else:
                print("You must enter a number from 1 to 6. Try again.")
        else:
            print("You must enter a number from 1 to 6. Try again.")
    return guess

def coin_flip():
    guess = guess_coin_side()
    answers = ["Heads", "Tails"]
    rand_flip = random.choice(answers)
    if (rand_flip == "Heads" and guess == "Tails") or (rand_flip == "Tails" and guess == "Heads"):
        print(guess + ", was the incorrect guess! Please try again.")
    else:
        print(guess + ", was the correct guess!")
    coin_flip()

def dice_roll():
    numerical_score = 0
    guess = guess_dice_roll()
    answer = random.randint(1, 6)
    if answer == guess:
        #dice_roll_score.append([guess, numerical_score])
        print(str(guess) + ", was the correct guess!")
    else:
        print(str(guess) + ", was the incorrect guess! Please try again.")
    dice_roll()

def display_scores():
    pass

main()
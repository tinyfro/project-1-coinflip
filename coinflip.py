#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""coinflip.py: Affectionately named 'coinflip', but includes a dice roll game. Educational project. Just for fun. Kinda got some help from ChatGPT but we won't speak about that..."""

__author__      = "Adam Zulic"
__copyright__   = "Copyright 2023, tinyfro"

import random, os

scores = {"coin_flip": [], "dice_roll": []}

def main():
    """Main function that runs the program"""
    scores["coin_flip_total"] = 0
    scores["dice_roll_total"] = 0
    main_menu()

def clear_cns():
    return os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    """Displays the main menu with options for the user to choose from"""
    while True:
        clear_cns()
        choice = input("Welcome to the games menu. Please choose a number to make a choice:\n1. Play Coinflip\n2. View Coinflip scores\n3. Play Diceroll\n4. View Diceroll scores\n5. Exit\n")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                clear_cns()
                coin_flip()
            elif choice == 2:
                clear_cns()
                display_scores("coin_flip")
            elif choice == 3:
                dice_roll()
            elif choice == 4:
                clear_cns()
                display_scores("dice_roll")
            elif choice == 5:
                exit()
            else:
                print("To make a choice, please choose the corresponding number.")

def guess_coin_side():
    """Asks the user to guess which side of a coin landed facing up"""
    while True:
        clear_cns()
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
    """Asks the user to guess the number that a dice rolled"""
    while True:
        clear_cns()
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
    """Flips a coin and keeps track of the user's score"""
    while True:
        guess = guess_coin_side()
        answers = ["Heads", "Tails"]
        rand_flip = random.choice(answers)
        if (rand_flip == "Heads" and guess == "Tails") or (rand_flip == "Tails" and guess == "Heads"):
            print(guess + ", was the incorrect guess! Please try again.")
            scores["coin_flip_total"] += 1
        else:
            print(guess + ", was the correct guess!")
            scores["coin_flip"].append(1)
            scores["coin_flip_total"] += 1
        if input("Do you want to continue playing? (y/n) ").lower() == 'n':
            break

def dice_roll():
    """Rolls a dice and keeps track of the user's score"""
    while True:
        guess = guess_dice_roll()
        answer = random.randint(1, 6)
        if answer == guess:
            scores["dice_roll"].append(1)
            scores["dice_roll_total"] += 1
            print(str(guess) + ", was the correct guess!\n")
        else:
            scores["dice_roll_total"] += 1
            print(str(guess) + ", was the incorrect guess! Please try again.\n")
        if input("Do you want to continue playing? (y/n) ").lower() == 'n':
            break

def display_scores(game):
    """Displays the user's scores for a specific game"""
    if game in scores:
        if scores[game]:
            print("Your score for {} is: {}/{} (Correct Guesses / Total Guesses)".format(game.title().replace("_", " "), sum(scores[game]), scores[game + "_total"]))
        else:
            print("You haven't played {} yet.\n".format(game.title().replace("_", " ")))
    else:
        print("Invalid game. Please choose a valid game.\n")
    input("Press Enter to go to the main menu...")

main()
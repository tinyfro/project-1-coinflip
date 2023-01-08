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


def generate_coin_flip():

    result = random.randint(1,2)

    if result == 1:
        return "Heads!"
    else:
        return "Tails!"


def guess_coin_flip():

    guess = input("Heads or Tails? ")

    if guess == "Heads" or "heads":
        guess_result(1)
    else:
        guess_result(2)


def guess_result(result):
    if generate_coin_flip() == "Heads!":
        print("Heads is correct!")
    else:
        print("Tails is correct!")

guess_coin_flip()
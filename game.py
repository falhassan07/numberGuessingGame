import random 
from art import logo 


print(logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100")


def guess_game():
    correct_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    is_game_over = False
    lives = 0

    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5


guess_game()
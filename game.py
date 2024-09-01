import random 
from art import logo 


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")


def guess_game():
    correct_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    is_game_over = False
    lives = 0

    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5


    while lives > 0 and not is_game_over:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != correct_guess:
            lives -= 1
            if guess < correct_guess:
                if lives > 0:
                    print("Too low. \nGuess again.")
                else:
                    print("Too low.")
            elif guess > correct_guess:
                if lives > 0:
                    print("Too High. \nGuess again.")
                else:
                    print("Too High.")
            if lives == 0:
                print("You've run out of guesses, you lose.")

        else:
            print(f"You got it!. The answer was {correct_guess}.")
            is_game_over = True


guess_game()
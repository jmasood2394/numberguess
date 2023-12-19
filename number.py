from random import randint
from art import logo
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Set difficulty level
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
# Compare the user's guess to the number chosen
def check_answer(usr_guess, answer, turns):
    """Takes the user's guess and compares it to the chosen number and returns a result."""
    if usr_guess > answer:
        print("Too high.") 
        return turns - 1
    elif usr_guess < answer:
        print("Too low.")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}.")
    
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    # Choose a number between 1 and 100
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    # set number of attempts based on difficulty level
    attempts = set_difficulty()    
    # Repeat until the user guesses correctly or runs out of attempts
    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # Ask the user to guess a number
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")

continue_game = True
while continue_game:
    play_game()
    continue_game = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if continue_game == 'n':
        os.system('clear')
        continue_game = False
    else:
        print("Good Bye!")    
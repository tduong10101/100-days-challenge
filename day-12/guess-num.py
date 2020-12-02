from art import logo
import random

HARD_DIFF = 5
EASY_DIFF = 10

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_DIFF
    else:
        return HARD_DIFF

def check_number(guess_numb,random_number):
    if guess_numb < random_number:
        print("Too low.")
        return 0
    elif guess_numb > random_number:
        print("Too high.")
        return 0
    else:
        print(f"You got it! The answer was {random_number}.")
        return 1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinkging of a number between 1 and 100.")
    random_number = random.randint(1,100)
    num_try = set_difficulty()
    for i in range(num_try):
        print(f"You have {num_try-i} attempts remaining to guess the number")
        guess_numb = int(input("Make a guess: "))
        check=check_number(guess_numb,random_number)        
        if num_try - i == 1:
            print("You've run out of guess, you lose.")
        elif check == 1:
            break
        else:
            print(f"Guess again.")

game()
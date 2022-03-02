# A simple guessing game that let's you guess a number in a given number of attempts
from guess_art import logo
import random
print(logo)

print("Welcome to the number's guessing game")
print("Pick a number between 1 and 100")
easy_attempts = 10
hard_attempts = 5

def difficulty():
    """takes no arguments, sets the difficulty level based on the user's choice and returns the number of attempts"""
    diff = input("Select a difficulty. Type 'easy' or 'hard' ")
    lives = 0
    if diff == "easy":
        lives += easy_attempts
    else:
        lives += hard_attempts
    return lives

attempts = difficulty()
print(f"You have {attempts} attempts for this game")


number = random.choice(range(1, 100))


def compare (guess, number):
    """" takes in two arguments and compares them"""
    if guess < 1 or guess > 100:
        print ("the number is out of range")
    elif guess > number:
        print("Higher than what's on my mind")
    elif guess < number:
            print ("Too low")
    else:
        print(f"you got it right,  {number} was on my mind")
    
#condition for game repetition
keep_guessing = True
while keep_guessing:
    guess = int(input("Make a guess: "))
    compare(guess, number)
    attempts -= 1
    #game termination condition
    if guess == number:
        keep_guessing = False
    elif attempts == 0:
        keep_guessing = False
        print(f"game over, you didn't get it {number}")
    else:
        print (f"You have {attempts} attempts left. Guess again ")
    
    
    
    
    
    



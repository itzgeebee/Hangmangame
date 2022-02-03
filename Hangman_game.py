
#import all needed modules
from hangman_art import logo, stages
from hangman_words import word_list
import random
from os import system
def clear():
    _ = system('cls')
#Generate a random word from the 'word_list'
word = random.choice(word_list)
#display the hangman logo
print(logo)
#create an empty list where your blanks would be generated
display = []
#loop through the words and add "_" to the "display" list for each letter of the word
for letters in word:
    display.append("_")
print(display)
#define a boolean variable that starts and stops the game
game_in_progress = True

lives = 6
#keep repeating all the steps in the while loop as long as the "game_in_progress" condition is true
while game_in_progress:
    guess = input("Guess a letter from the word \n")
    #if the guessed letter has been chosen, notify the player
    clear()
    if guess in display:
        print("You have already chosen that letter " + lett)
    #loop through the total number of letters in the word
    #find the numerical positions of the letters in word
    for position in range(len(word)):
        lett = word[position]
        #if the guessed letter is the same as a letter in the, replace "_" with that letter at the same position
        if guess == lett:
            display[position] = lett 
        
    if guess not in word:
        print("Letter is not in the word " + guess)
        lives -= 1
        print(f"You have {lives} lives left ")
        if lives ==1:
            print("Last chance to save me")
        if lives == 0:
            print("game is over, Thanks for trying to save me")
            print("here's the word " + word)
            game_in_progress = False
    print(display)  
    print(stages[lives])  
    if "_" not in display:
        print("You won, Thanks for saving me")
        game_in_progress = False
    


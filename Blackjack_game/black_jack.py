
from black_jack_art import logo
import random
from os import system

def clear():
    '''clears the terminal after each game'''
    _ = system('cls')

def deal_card():
    ''' Takes in no arguments and chooses a random number from the card list and assigns it to a "your card" variable '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_card = random.choice(cards)
    return your_card
            
def calculate_score(deck):
    '''adds the number on your cards together and replicates the behaviour of an "ace" card
    it returns the sum of the card'''
    if sum(deck) == 21 and len(deck) ==2:
        return 0

    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return  sum(deck)

def compare(user_score, comp_score):
    ''' a function that takes in two variables(user and computer score) and compares them to decide the winner
    returns different answers for different conditons'''
    if user_score > 21 and comp_score > 21:
        return "You went over, you lose"

    if user_score == comp_score:
        return "it's a draw"
    elif comp_score == 0:
        return "Lose, computer has blackjack"
    elif user_score == 0:
        return "You win, blackjack!!"
    elif user_score > 21:
        return "You went over, you lose"
    elif comp_score > 21:
        return "Comp went over, you win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    '''A function that contains the whole game.'''
    print(logo)
    #define the card variables and game continuation condition
    your_deck = []
    comp_deck = []
    game_on = True
    #iterates through a defined range and adds a card to the predefined lists
    for i in range(2):
        your_deck.append(deal_card())
        comp_deck.append(deal_card())
    #calculates user score while the game_on condition is still true
    while game_on:
        user_score = calculate_score(your_deck)
        comp_score = calculate_score(comp_deck)

        print(f"your cards: {your_deck}, your current score: {user_score}")
        print(f"computer's first card {comp_deck[0]}")

        #conditions for terminating game
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_on = False

        else:
            next_deal = input("hit or hold?: ")
            if next_deal == "hit":
                your_deck.append(deal_card())
            else:
                game_on = False
    #computer's playing strategy        
    while comp_score != 0 and comp_score < 17:
        comp_deck.append(deal_card())
        comp_score = calculate_score(comp_deck)
    print(f"   Your final hand: {your_deck}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_deck}, final score: {comp_score}")
    print(compare(user_score, comp_score))
#condition for playing new game
while input("do you want to play a game of blackjack? 'y' or 'n': ") == 'y':
 
    clear()
    play_game()








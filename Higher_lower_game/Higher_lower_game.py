from os import system
from Hl_art import logo, vs
from HL_dictionary import data
import random
def clear():
    _ = system('cls')
def game():
    print(logo)
    print("Welcome to the higher lower game, you have to select the account with higher follower count")
    player_score = 0
    second = random.choice(data)
    game_on = True
    while game_on:
        #declare two new dictionaries randomly and store them 
        first = second
        second = random.choice(data)
        #check if the second second variable is the same as the first and change it to a different one 
        if second == first:
            second = random.choice(data)
    
        #show the user the selected brands except the follower's count
        def format_account(account):
            '''takes in one argument and returns it in the game format'''
            account_name = account["name"]
            account_desc = account["description"]
            account_country = account["country"]
            return (f"Account: {account_name}, Description: {account_desc}, Country: {account_country} ")
        acc_a = format_account(first)
        acc_b = format_account(second)

        print(acc_a)
        print(vs)
        print(acc_b)
            
        answer = input("higher or lower: ").lower()

        #define a function that collects user answer and compares first with second account
        def compare(answer, first, second):
            '''takes in 3 arguments and returns true or false if answer is right or wrong'''
            if first["follower_count"] > second["follower_count"]:
                return answer == "higher"
            else:
                if second["follower_count"] > first["follower_count"]:
                    return answer == "lower"
        #increment player score if the user gets the answer correctly           
        outcome = compare(answer, first, second)
        if outcome:
            player_score += 1
            clear()
            print(f"You're correct. Your score: {player_score}")
            print(second)
        #game termination condition   
        else:
            game_on = False
            print(f"you are wrong. Your score: {player_score} ")
            print(first)
            print(second)
while input("do you want to test your instagram knowledge with this awesome game? Y/N: ").lower() == 'y':
    game()
        

        
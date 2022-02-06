from os import system

from auction_art import logo

def clear():
    _ = system('cls')

print(logo)
#declare your dictionary and condition for the code to run
bid_details = {}
to_continue = True


#defines a function to check for the highest bidder using for loop
def highest_bidder(bidding_rec):
  bid_value = 0
  winner = ""
  for b in bidding_rec:
      bid_amount =  bidding_rec[b]
      if bid_amount >  bid_value:
        bid_value = bid_amount
        winner = b

  print(f"The winner is {winner}, with a bid of ${bid_value}")
#collect information from the user as long as the "to_continue" condition is true
while to_continue:
  name = input("please enter your name\n")
  bid =int(input(f"please enter bid amount \n $"))
  bid_details[name] = bid
  clear()
  next_bidder = input("Is there another bidder? Please type 'yes' or 'no' \n").lower()
  #end the bid and print the winner of the bid if the "to_continue" condition becomes false
  if next_bidder == "no":
    to_continue = False
    highest_bidder(bid_details)
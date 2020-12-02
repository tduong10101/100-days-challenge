############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

import random
from art import logo
from os import name, system
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play = ""
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
def deal(num_deal):
    deal_cards = []
    for i in range(num_deal):
        deal_cards.append(random.choice(cards))
    return deal_cards
def switch_ace(input_cards):
    while (sum(input_cards) > 21) and (11 in input_cards):
        for i in range(len(input_cards)):
            if input_cards[i] == 11:
                input_cards[i] = 1
                break
    return input_cards
start_message="Do you want to play a game of black jack? 'y' or 'n': "
while play != 'n':
    while not (play == 'y' or play == 'n'):
        play = input(start_message)
    if play == 'y':
        default_deal = 2
        player_cards = []
        computer_cards = []
        player_score = computer_score = 0
        clear()
        print(logo)
        cont_deal = True
        end_game = False
        
        while not end_game:
            while cont_deal:            
                if len(player_cards) < 2:
                    num_deal = default_deal
                    computer_cards.extend(deal(num_deal))
                else:
                    num_deal = 1
                
                player_cards.extend(deal(num_deal))
                player_score = sum(player_cards)
                
                if (player_score > 21) and (11 in player_cards):
                   player_cards = switch_ace(player_cards)
                   player_score = sum(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                if player_score > 21:
                    end_message = "You lose!"
                    end_game = True
                    break
                
                cont_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if cont_deal == 'y':
                    cont_deal = True
                elif cont_deal == 'n':
                    cont_deal = False
            computer_score = sum(computer_cards)
            print(f"Computer's cards: {computer_cards}, with score: {computer_score}")
            if (computer_score > 21) and (11 in computer_cards):
                    computer_cards = switch_ace(computer_cards)
            if not end_game:                
                while computer_score < 16:
                    computer_cards.extend(deal(1))
                    computer_score = sum(computer_cards)
                    if (computer_score > 21) and (11 in computer_cards):
                        computer_cards = switch_ace(computer_cards)

                if computer_score > 21:
                    end_message = "You Win!"
                elif computer_score < player_score:
                    end_message = "You Win!"
                elif computer_score == player_score:
                    end_message = "It's a draw!"
                else:
                    end_message = "You Lost!"

            print(f"{end_message}\nYour cards are {player_cards}, with score {player_score}.\nComputer's cards are {computer_cards}, with score {computer_score}")
            break  

    start_message = "Do you want to play another game of black jack? 'y' or 'n': "
    play = ""

                


# A program that plays blackjack from the user vs the computer.

# =============  Our Blackjack House Rules ===================

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# If the card total is less the 17, then player must get another card

import os
import random

import art


def clear():
    # clears the screen
    clear_command = "clear"
    if os.name == "nt":
        clear_command = "cls"
    os.system(clear_command)


def deal_card(player_cards):
    # deals a random card to a card list
    # user is a list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    # if player pulls ace and total is more than 10, ace is now a 1
    if card == 11 and card_total(player_cards) > 10:
        card = 1

    player_cards.append(card)


def card_total(cards):
    # calculates the total of a list of integers
    # cards is a list of integers
    return sum(cards)


def print_final_score(user_cards, computer_cards):
    # prints the cards and final score of cards of user and computer
    # user_cards is a list
    # computer_cards is a list
    user_total = card_total(user_cards)
    computer_total = card_total(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_total}")


def play_game():

    # Initialize  player
    user_cards = []
    computer_cards = []

    # Deal two cards to each player
    for _ in range(2):
        deal_card(user_cards)
        deal_card(computer_cards)

    # If computer hand is less than 17, then deal another card to computer
    while card_total(computer_cards) < 17:
        deal_card(computer_cards)

    # Keep dealing card to user until user passes or goes past 21
    end_game = False
    while not end_game:
        # Show current user hand and first card from computer
        print(f"Your cards: {user_cards}, current score: {card_total(user_cards)}")
        print(f"Computer first card: {computer_cards[0]}")

        grab_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if grab_card == "y":
            deal_card(user_cards)

            # If card dealt makes user go over, end game
            if card_total(user_cards) > 21:
                print_final_score(user_cards, computer_cards)
                print("You've gone over 21! You lose.")
                end_game = True

        elif grab_card == "n":
            user_total = card_total(user_cards)
            computer_total = card_total(computer_cards)
            print_final_score(user_cards, computer_cards)
            if user_total > computer_total or computer_total > 21:
                print("You win! :)")

            # user draws with computer
            elif user_total == computer_total:
                print("Draw! :|")

            else:
                print("You lose! :(")

            end_game = True


def main():
    end_game = False
    while not end_game:
        continue_game = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': "
        ).lower()
        if continue_game == "y":
            clear()
            print(art.logo)
            play_game()
        else:
            end_game = True


main()

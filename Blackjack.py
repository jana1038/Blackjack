# Blackjack
# Jana Kosková
# 27. 1. 2021


import random
import numpy as np
import sys


while True:
    card_set = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","K","K","K","K","Q","Q","Q","Q","A","A","A","A"]
    # welcome to Blackjack
    starting_input = input("WELCOME TO Blackjack! Press enter to start (type exit to exit program)")

    # When the user types exit, it exits the program
    if starting_input == "exit":
        sys.exit()

    def generate_card_and_value():
        card = random.choice(card_set)
        if card == "J":
            value = 10
        elif card == "K":
            value = 10
        elif card == "Q":
            value = 10
        elif card == "A":
            value = 11
        else:
            value = card
        # delets generated card from card_set
        card_set.remove(card)

        return card, value

    # dealer's cards
    dealer_first_card, dealer_first_value = generate_card_and_value()
    dealer_second_card, dealer_second_value = generate_card_and_value()
    dealer_cards_hidden = ["x",dealer_second_card]
    print("dealer has: ", dealer_cards_hidden)


    # player's Cards
    player_first_card, player_first_value = generate_card_and_value()
    player_second_card, player_second_value = generate_card_and_value()

    # saving player's card to the list
    player_cards_for_showing = [player_first_card, player_second_card]
    player_cards_for_summing = [player_first_value, player_second_value]
    dealer_cards_for_showing = [dealer_first_card, dealer_second_card]
    dealer_cards_for_summing = [dealer_first_value, dealer_second_value]
    print("you have ", player_cards_for_showing)

    def print_card_assessment():
        print("you have", player_cards_for_showing)
        print("Your sum is ", np.sum(player_cards_for_summing))
        print("dealer has", dealer_cards_for_showing)
        print("dealer's sum is", np.sum(dealer_cards_for_summing))

    # start of game, player knows his two cards and one dealer card
    counter = 0
    while True:
        counter += 1
        print("===============")
        print("Round number "+str(counter))
        print("===============")
        # player decides if he takes another card or not
        question = str(input("Do you want to  \"hit\" or \"stay?\"  ")).lower()
        if question == "hit":
            player_new_card, player_new_value = generate_card_and_value()
            player_cards_for_showing.append(player_new_card)
            player_cards_for_summing.append(player_new_value)

            if np.sum(player_cards_for_summing) > 21:
                print_card_assessment()
                print("You lost because you have more than 21.")
                break
            print("you have", player_cards_for_showing)


        if question == "stay":
            # when player stops playing, dealer takes cards up to sum 17
            while True:
                if np.sum(dealer_cards_for_summing) > 21:
                    break
                elif np.sum(dealer_cards_for_summing) < 17:
                    dealer_new_card, dealer_new_value = generate_card_and_value()
                    dealer_cards_for_showing.append(dealer_new_card)
                    dealer_cards_for_summing.append(dealer_new_value)
                else:
                    break

            if np.sum(dealer_cards_for_summing) > 21:
                print_card_assessment()
                print("You won because dealer has too much.")
            elif (np.sum(player_cards_for_summing))>(np.sum(dealer_cards_for_summing)):
                print_card_assessment()
                print("You are a winner because you have better cards than dealer.")
            elif (np.sum(player_cards_for_summing)) == (np.sum(dealer_cards_for_summing)):
                print_card_assessment()
                print("It's a draw")
            else:
                print_card_assessment()
                print("You lost because the dealer has better cards.")
            break

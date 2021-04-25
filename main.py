from build_deck import full_deck
from sys import exit
import random
import time

# card set no. 4, 13, 52

dealer_cards_value = {"Dealer": 0}
player_cards_value = {}
ask_name = input("What is your name?\n")
player_cards_value[ask_name] = 0
player_cards = {}
dealer_cards = {}

amount_in_pot = 1000
money_pot = "£{amount}".format(amount=amount_in_pot)
bet = 0
restart = 0

new_dict = {}
new_dict2 = {}
key_deck_list = [key for key in full_deck.keys()]
value_deck_list = [value for value in full_deck.values()]
hit = 0

while True:
    player_turn = 0
    dealer_turn = 0

    if hit < 1:
        
        print(
            "Hi {name}! Welcome to Casino Royale!\n"
            "Player has £{pot} to play with.".format(name=ask_name, pot=amount_in_pot)
            )

        while True:
            confirm_prompt = input("Would you like to continue? Y/N\n")
            if confirm_prompt.upper() == "Y" and type(confirm_prompt) != int:
                bet_prompt = input("How much would you like to bet? Current amount £{0}\n".format(amount_in_pot))
                try:
                    int(bet_prompt)
                    if int(bet_prompt) in range(1, amount_in_pot):
                        bet_confirm_prompt = input("You bet £{0}, are you happy to continue? Y/N:\n".format(bet_prompt))
                        if bet_confirm_prompt.upper() == "Y" and type(confirm_prompt) != int:
                            amount_in_pot -= int(bet_prompt)
                            bet += int(bet_prompt)
                            print("You have now placed a bet for £{0}, and have £{1} left remaining in your pot.".format(bet, amount_in_pot))
                            begin_game = input("Ready to play? Y/N:\n")
                            if begin_game.upper() == "Y" and type(begin_game) != int:
                                time.sleep(1)
                                shuffle = print("\nShuffling...")
                                time.sleep(3)
                                dealing = print("\nNow dealing cards...")
                                time.sleep(3)
                                break
                            else:
                                amount_in_pot += int(bet)
                                bet -= int(bet_prompt)
                                continue
                    else:
                        print("You do not have enough.")
                        continue
                except ValueError:
                    print("You need to place the right bet amount.")
                    continue
            elif confirm_prompt.upper() == "N" and type(confirm_prompt) != int:
                print("Thanks for playing!")
                exit()
            else:
                print("Wrong button.")
                continue
        # Deck gets shuffled and cards get passed out. Player gets the first two cards.
        if player_turn > 0:
            new_dict.clear()
    else:
        player_turn += 1
        pass

    while True:
        four_random = random.sample(range(0, len(full_deck)), 4)
        if player_turn > 0:
            player_cards[key_deck_list[four_random[0]]] = value_deck_list[four_random[0]]
            player_cards_lst = list(player_cards.values())
            player_cards_value[ask_name] = sum(player_cards_lst)
        else:
            player_cards[key_deck_list[four_random[0]]] = value_deck_list[four_random[0]]
            player_cards[key_deck_list[four_random[1]]] = value_deck_list[four_random[1]]
            player_cards_lst = list(player_cards.values())
            player_cards_value[ask_name] = sum(player_cards_lst)
        
        for key, value in full_deck.items():
            if key not in list(player_cards.keys()):
                new_dict[key] = value
        
        time.sleep(3)
        print(
            "Your cards:" + str(player_cards) + "\n" \
            "Total value for Player: " + str(player_cards_value)
            )
            
        if sum(player_cards.values()) == 21:
            print(ask_name + " got 21! you Win!!!")
            amount_in_pot += bet * 2
            bet = 0
            new_prompt = input("Would you like to continue? Y/N\n")
            if new_prompt == "Y" and type(new_prompt) != int:
                player_turn += 6
                break
            else:
                exit()
        else:
           break
        if player_turn > 5:
            player_turn = 0
            exit()
    if sum(player_cards.values()) > 21:
        print("You Burst, too bad Game Over!\n")
        bet = 0
        hit = 0
        player_cards.clear()
        dealer_cards.clear()
        continue
    else:
        pass
        # Dealer gets his cards and shows the first one and on the second turn shows the second card.
        time.sleep(3)
        print("\nNow wait for the dealer.")
        time.sleep(3)
        if dealer_turn < 1 and player_turn < 1:
            dealer_cards.clear()
            dealer_cards[key_deck_list[four_random[2]]] = value_deck_list[four_random[2]]
            dealer_cards[key_deck_list[four_random[3]]] = value_deck_list[four_random[3]]
            dealer_cards_lst = list(dealer_cards.values())
            dealer_cards_value["Dealer"] = sum(dealer_cards_lst)
            dealer_first, dealer_second = list(dealer_cards.items())
            if dealer_turn < 1:
                print("Dealer shows 1st card " + str(dealer_first[0]) + " Total value: {}".format(dealer_cards[dealer_first[0]]))
                dealer_turn += 1
                pass
        else: 
            print("Dealer shows 2nd card " + str(dealer_second[0]) + "Total value: {}".format(dealer_cards[dealer_second[0]]))
            time.sleep(3)
            print("All cards: " + str(dealer_cards) + " Total Value: " + str(sum(dealer_cards.values())))
        
        for key, value in new_dict.items():
            if key not in list(dealer_cards.keys()):
                new_dict2[key] = value

        while True:
            turn_prompt = input("\nWhat would you like to do? Hit or Stay. H/S:\n")
            if turn_prompt.upper() == "S" and type(turn_prompt) != int:
                if sum(player_cards.values()) > sum(dealer_cards.values()):
                    print("Dealers cards: " + str(dealer_cards))
                    time.sleep(2)
                    print("You win! Congrats")
                    amount_in_pot += bet * 2
                    bet = 0
                    new_input = input("Would you like to restart? Y/N:\n")
                    if new_input == "Y" and type(new_input) != int:
                       restart += 1
                       break
                    else:
                        exit()
                elif len(player_cards) > len(dealer_cards):
                    print("You Win! yeeeehaaaa!")
                    amount_in_pot += bet * 3
                    bet = 0
                    new_input = input("Would you like to restart? Y/N:\n")
                    if new_input == "Y" and type(new_input) != int:
                       restart += 1
                       break
                    else:
                        exit()
                else:
                    print("Dealers Cards: " + str(dealer_cards))
                    print("You lose!")
                    bet = 0
                    restart += 1
                    break
            elif turn_prompt.upper() == "H" and type(turn_prompt) != int:
                player_turn += 1
                hit += 1
                break
            else:
                print("Wrong Key Pressed.")
                continue
        if player_turn > 0:
            continue
    if restart > 0:
        restart = 0    
        player_cards.clear()
        dealer_cards.clear()
        new_dict.clear()
        new_dict2.clear()
        continue
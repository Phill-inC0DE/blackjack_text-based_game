from build_deck import full_deck
import random
import time
# card set no. 4, 13, 52

dealer_cards_value = {"Dealer": 0}
player_cards_value = {}
ask_name = input("What is your name?\n")
player_cards_value[ask_name] = 0

amount_in_pot = 1000
money_pot = "£{amount}".format(amount=amount_in_pot)
bet = 0
player_turn = 0
dealer_turn = 0
player_cards = {}
dealer_cards = {}


print(
    "Hi {name}! Welcome to Casino Royale!\n"
    "New comers get £1000 to play with.".format(name=ask_name)
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

key_deck_list = [key for key in full_deck.keys()]
value_deck_list = [value for value in full_deck.values()]

four_random = random.sample(range(0, 52), 4)
player_cards[key_deck_list[four_random[0]]] = value_deck_list[four_random[0]]
player_cards[key_deck_list[four_random[1]]] = value_deck_list[four_random[1]]
player_cards_lst = list(player_cards.values())
player_cards_value[ask_name] = sum(player_cards_lst)

print(
    "Your cards:" + str(player_cards) + "\n" \
    "Total value for Player: " + str(player_cards_value)
    )

time.sleep(3)
print("\nNow wait for the dealer.")
time.sleep(3)
dealer_cards[key_deck_list[four_random[2]]] = value_deck_list[four_random[2]]
dealer_cards[key_deck_list[four_random[3]]] = value_deck_list[four_random[3]]
dealer_cards_lst = list(dealer_cards.values())
dealer_cards_value["Dealer"] = sum(dealer_cards_lst)
print("\nDealer shows: " + str(dealer_cards) + " total value: {}".format(dealer_cards_value.get("Dealer")))
prompt = input("\nWhat would you like to do? Hit or Stay.\n")
from build_deck import full_deck
import random
# card set no. 4, 13, 52

dealer_cards_value = {"Dealer": 0}
player_cards_value = {}
ask_name = input("What is your name? ")
player_cards_value[ask_name] = 0

amount_in_pot = 0
money_pot = "£{amount}".format(amount=amount_in_pot)
player_turn = 0
dealer_turn = 0
player_cards = {}
dealer_cards = {}

key_deck_list = [key for key in full_deck.keys()]
value_deck_list = [value for value in full_deck.values()]

while True:
    four_random = random.sample(range(0, 52), 4)
    player_cards[key_deck_list[four_random[0]]] = value_deck_list[four_random[0]]
    player_cards[key_deck_list[four_random[1]]] = value_deck_list[four_random[1]]
    player_value = player_cards.values()
    player_total_value = sum(player_value)
    player_cards_value[ask_name] = player_total_value
    if len(player_cards) == 2:
        dealer_cards[key_deck_list[four_random[2]]] = value_deck_list[four_random[2]]
        dealer_cards[key_deck_list[four_random[3]]] = value_deck_list[four_random[3]]
        dealer_values = dealer_cards.values()
        dealer_total_value = sum(dealer_values)
        dealer_cards_value["Dealer"] = dealer_total_value
    elif len(dealer_cards) == 2 and len(player_cards) == 2:
        print("Dealer shows: " + str(dealer_cards) + " total value: {}".format(dealer_cards_value.get("Dealer")))
        prompt = input("What would you like to do? Hit or Fold. ")
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
bet_prompt = 0
player_cards = {}
dealer_cards = {}

def check_for_int(command):
    while True:
        try:
            if command <= amount_in_pot:
                int(command)
                return command
        except ValueError:
            print("Type in a number.")
            command = 0
            return command


print(
    "Hi {name}! Welcome to Casino Royale!\n"
    "New comers get £1000 to play with.".format(name=ask_name)
    )
while True:
    confirm_prompt = input("Would you like to continue? Y/N\n")
    if confirm_prompt.upper() == "Y" and not int:
        bet_prompt = input("How much would you like to bet? Current amount £{0}\n".format(amount_in_pot))
        bet_confirm_prompt = input("You bet £{0}, is this correct? Y/N:\n".format(check_for_int(int(bet_prompt))))
        if bet_confirm_prompt.upper() == "Y" and int(bet_prompt) > 0:
            amount_in_pot -= int(bet_prompt)
            bet += int(bet_prompt)
            print("You have now placed a bet for £{0}, and have £{1} left remaining in your pot.".format(bet, amount_in_pot))
            begin_game = input("Ready to play? Y/N:\n")
        else:
            print("You need to place a bet.")
        if begin_game.upper() == "Y":
            time.sleep(1)
            shuffle = print("\nShuffling...")
            time.sleep(3)
            dealing = print("\nNow dealing cards...")
            time.sleep(3)
            break

key_deck_list = [key for key in full_deck.keys()]
value_deck_list = [value for value in full_deck.values()]

four_random = random.sample(range(0, 52), 4)
player_cards[key_deck_list[four_random[0]]] = value_deck_list[four_random[0]]
player_cards[key_deck_list[four_random[1]]] = value_deck_list[four_random[1]]
player_cards_value[ask_name] = sum(player_cards.values())
print(
    "Your cards:" + str(player_cards) + "\n" \
    "Total value for Player: " + str(player_cards_value)
    )

time.sleep(5)
print("\nNow wait for the dealer.")
time.sleep(5)

dealer_cards[key_deck_list[four_random[2]]] = value_deck_list[four_random[2]]
dealer_cards[key_deck_list[four_random[3]]] = value_deck_list[four_random[3]]
dealer_cards_value["Dealer"] = sum(dealer_cards.values())
print("\nDealer shows: " + str(dealer_cards) + " total value: {}".format(dealer_cards_value.get("Dealer")))
prompt = input("\nWhat would you like to do? Hit or Stay.\n")
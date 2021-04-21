from script import full_deck
import random
# card set no. 4, 13, 52

full_deck_dict = full_deck
full_deck_list = [key + " - Value: " + str(value) for key, value in full_deck_dict.items()]
shuffle_deck = [random.randint(0, len(full_deck_list)-1), random.randint(0, len(full_deck_list)-1)]

print(full_deck_list[shuffle_deck[0]]," | ", full_deck_list[shuffle_deck[1]])
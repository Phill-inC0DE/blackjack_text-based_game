# Stage 1 / set up as an array, with four arrays (one for each suit)
value_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #13
suit_to_cards = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
type_of_cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Queen', 'King', 'Jack']

class MakeSuit:
    def __init__(self, suit_card, type_card , value_card):
        self.suit_card = suit_card
        self.type_card = type_card
        self.value_card = value_card

make_suit = MakeSuit(suit_to_cards[0:], type_of_cards[0:], value_cards[0:])

def create_suit(suit_index):
    return [make_suit.type_card[c] + " of " + make_suit.suit_card[suit_index] for c in range(0, 13)]

heart_suit = create_suit(0)
club_suit = create_suit(1)
diamond_suit = create_suit(2)
spade_suit = create_suit(3)
all_suits = [heart_suit, club_suit, diamond_suit, spade_suit]

def add_value(card_suits):
    total_deck = {}
    total_deck.update({key:value for key, value in zip(card_suits[0], make_suit.value_card[0:])})
    total_deck.update({key:value for key, value in zip(card_suits[1], make_suit.value_card[0:])})
    total_deck.update({key:value for key, value in zip(card_suits[2], make_suit.value_card[0:])})
    total_deck.update({key:value for key, value in zip(card_suits[3], make_suit.value_card[0:])})
    return total_deck

full_deck = add_value(all_suits)
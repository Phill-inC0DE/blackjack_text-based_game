import random
import time
import datetime
from sys import exit

# SUIT, RANK AND VALUE ARRAYS
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Queen", "King", "Jack", "Ace"]
values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, 
    "Ten": 10, "Queen": 10, "King": 10, "Jack": 10, "Ace": 11,
    }

# WORKS OUT THE TIME IN THE DAY AND ADJUST THE GREETING TO EITHER MORNING, AFTERNOON OR EVENING.
def what_time():
    date_time = str(datetime.datetime.now().time())
    date_time = int(date_time[:2])
    if date_time < 12 and date_time > 00:
        return "Good morning! "
    elif date_time > 12 and date_time < 18:
        return "Good afternoon! "
    else:
        return "Good evening! "

# PLACEHOLDERS FOR PROMPTING WHEN TO RESTART THE GAME, CARRY ON PLAYING, THE START UP GREETING AND WHO WINS.
greeting = what_time()
playing = True
restart = 0
player_win = False
dealer_win = False

# ASKS USER FOR NAME & ADJUST NAME SO IT BEGINS WITH A CAPITAL.
name = input("\n" + greeting + "What's your name?\n")
print("\nHi {name}! Welcome to the Casino!".format(name=name[0].upper() + name[1:]))
name = name[0].upper() + name[1:]
time.sleep(3)

# CLASS: BUILDS EACH CARD
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

# CLASS: MAKES AN ARRAY OF ALL THE CARDS AND PLACES THEM INTO THE DECK. IT ALSO SHUFFLES AND DEALS THE CARDS.
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n " + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# CLASS: BUILD AN ARRAY FOR THE PLAYER & DEALER WITH THE CARDS THEY WHERE DELT FROM THE PREVIOUS CLASS AND WORKS OUT THE VALUES. 
# ALSO, IT CHECKS THE PLAYER & DEALERS HAND FOR ANY ACES AND ADJUST THE VALUE ACCORDINGLY.
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces  = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# CLASS: THIS BUILDS THE PLAYERS CHIPS THEY WISH TO BET WITH. I ALSO ADDED THE EXTRA FEATURES THAT ALLOWS THE PLAYER TO TAKE OUT A SMALL LOAN
# AND GO INTO DEBT (AS A SHORT OF HIDDEN EXTRA LIFE TO CARRY ON THE GAME) THEY ONLY GET AN EXTRA 1000 BEFORE ITS COMPLETELY GAME OVER.
class Chips:
    def __init__(self):
        self.total = round(1000.00)
        self.bet = round(0.00)
        self.debt = round(0.00)
        self.debt_count = 0
        self.loan = 1000
    
    def win_bet(self):
        self.total += round(self.bet * 1.5)
    
    def lose_bet(self):
        self.total -= self.bet
    
    def pay_debt(self):
        self.debt += round(self.bet * 1.5) / 2
        self.total += round(self.bet * 1.5) / 2

deck = Deck()
deck.shuffle()

player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand = Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

# THIS FUNCTION WAS THE MOST COMPLEX, IT WORKS OUT WHETHER OR NOT THE PLAYER HAS NO CHIPS LEFT, OR IF THEY WANT TO PLACE A BET WITH THE CHIPS THEY HAVE.
# AND IF THEY HAVE NO CHIP THEY WILL THEN BE ASKED IF THEY WANT TO TAKE OUT A LOAN.
def take_bet(chips):
    while True:
        number_str = "1234567890"
        chips.bet = 0
        try:
            chips.bet = int(input('\nHow many chips would you like to bet {1}? you have {0} chips avaliable.\n'.format(round(chips.total), name)))
            if chips.bet < chips.total and restart < 1:
                print("Each chip is worth £1 and every win rewards you with 1.5x the amount you bet.")
                time.sleep(3)
                print("Lets begin.")
                time.sleep(2)
                print("Dealing cards...")
                time.sleep(2)
        except ValueError:
            print('Sorry, a bet must be a digit.')
            continue
        if chips.total < 1:
            print("You lost all your chips!")
            time.sleep(3)
            if chips.loan > 0:
                loan_choice = input("Would you like to take out a small loan? Y/N\n")
                if loan_choice.lower() == 'y':
                    try:
                        choice = int(input("\nHow many chips do you want? you have up to {0} avaliable. ".format(str(chips.loan))))
                        if choice <= chips.loan and choice > 0:
                            print("\nIf you lose all the loan money avaliable, you're done for the day.")
                            time.sleep(3)
                            print("You borrowed {0} chips.".format(choice))
                            time.sleep(3)
                            chips.total += choice
                            chips.debt -= choice
                            chips.loan += chips.debt
                            chips.debt_count += 1
                            continue
                        else:
                            print("You can't have that amount.")
                            continue
                    except ValueError:
                        print('Sorry, amount must be a digit.')
                        continue
                elif str(loan_choice[0]) in number_str or type(loan_choice) == int:
                    print('Sorry, please enter a valid response.')
                    continue
                else:
                    print("Okay it's GAME OVER.\n")
                    exit()
            else:
                print("Your done! Get out!\n\nGAME OVER\n")
                exit()
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet cannot exceed the amount you hold.")
            else:
                break

# HITS THE HAND WITH A CARD DELT FROM THE DECK AND ADJUSTS FOR THE ACE. 
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# WORKS OUT IF THE PLAYER WISHES TO HIT OR STAND.
def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('\nWould you like to hit or stand? Press H/S\n')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('{0} stands. Dealer is playing.'.format(name))
            playing = False
        else:
            print('Sorry, please enter a valid response.')
            continue
        break

# ASKS IF YOU WANT TO RESTART OR END THE GAME.
def end_of_game():
    number_str = "1234567890"
    while True:
        new_game = input("\nWould you like to play another hand? Press Y/N\n")
        try: 
            if new_game[0].lower() == "y":
                return 1, True    
            elif str(new_game[0]) in number_str or type(new_game) == int:
                print('Sorry, please enter a valid response.')
                continue
            else:
                print("Thanks for playing.")
                exit()
        except IndexError:
            print('The wrong key was pressed.')

# HIDES ONE OF THE DEALERS CARDS IN THE BEGINNING OF THE GAME, AND ALL OF THE PLAYERS CARDS.
def show_some(player, dealer):
    print("______________________")
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    time.sleep(3)
    print("______________________")
    print("\n{0}'s Hand:".format(name), *player.cards, sep='\n ')
    print("Your value:", player.value)

# SHOWS ALL OF THE DEALERS AND PLAYERS CARDS ON THE NEXT RUN THROUGH.
def show_all(player, dealer):
    print("______________________")
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's value:", dealer.value)
    time.sleep(3)
    print("______________________")
    print("\n{0}'s Hand:".format(name), *player.cards, sep='\n ')
    print("Your value:", player.value)

# WORKS OUT IF THE PLAYERS HAS BUST AND ADJUSTS WHO WON & LOST.
def player_busts(player, dealer, chips, player_win, dealer_win):
    print("{0} busts!".format(name))
    player_win = False
    dealer_win = True
    chips.lose_bet()
    return player_win, dealer_win

# THE NEXT FOUR FUNCTIONS DO SIMILAR TO THE ABOVE FUNCTION...
def player_wins(player, dealer, chips, player_win, dealer_win):
    if player_chips.debt < 0:
        print("\n{0} wins!".format(name))
        time.sleep(3)
        player_win = True
        dealer_win = False
        chips.pay_debt()
        return player_win, dealer_win
    else:
        print("\n{0} wins!".format(name))
        time.sleep(3)
        player_win = True
        dealer_win = False
        chips.win_bet()
        return player_win, dealer_win

def dealer_busts(player, dealer, chips, player_win, dealer_win):
    if player_chips.debt < 0:
        print("Dealer busts!")
        print("\n{0} wins!".format(name))
        time.sleep(3)
        player_win = True
        dealer_win = False
        chips.pay_debt()
        return player_win, dealer_win
    else:
        print("Dealer busts!")
        print("\n{0} wins!".format(name))
        time.sleep(3)
        player_win = True
        dealer_win = False
        chips.win_bet()
        return player_win, dealer_win

def dealer_wins(player, dealer, chips, player_win, dealer_win):
    print("\nDealer wins!")
    player_win = False
    dealer_win = True
    chips.lose_bet()
    return player_win, dealer_win

def push(player, dealer, player_win, dealer_win):
    player_win = False
    dealer_win = False
    return player_win, dealer_win

player_chips = Chips()

# THIS WHILE LOOP ALLOWS A RUN THROUGH OF THE GAME AND RESTART IT WITHOUT HAVING TO RERUN THE SCRIPT.
while playing:
        
        if restart > 0:
            deck = Deck()
            deck.shuffle()
            player_hand = Hand()
            dealer_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        if player_chips.debt_count > 0:
            take_bet(player_chips)
            debt_count = player_chips.debt_count
            print("\nDebt still owed: £" + str(round((player_chips.debt - (player_chips.debt * 2)))))

        else:    
            take_bet(player_chips)
        
        debt_count = player_chips.debt_count
        restart = 0
        show_some(player_hand, dealer_hand)
        time.sleep(3)
        hit_or_stand(deck, player_hand)
        show_all(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_win, dealer_win = player_busts(player_hand, dealer_hand, player_chips, player_win, dealer_win)
            print("\nYou LOSE:\n£{0}".format(round(player_chips.bet)))
            time.sleep(3)
            restart, playing = end_of_game()
            if restart > 0 and playing == True:
                continue
            else:
                break

        if playing == True:    
            if player_hand.value < 20 and dealer_hand.value < 17:
                while dealer_hand.value < 17 and player_hand.value < 20:
                    hit(deck, dealer_hand)
                    hit_or_stand(deck, player_hand)
                    show_all(player_hand, dealer_hand)
                    time.sleep(3)
            elif player_hand.value >= 20 and dealer_hand.value < 17:
                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)
                    show_all(player_hand, dealer_hand)
                    time.sleep(3)
            elif player_hand.value < 20 and dealer_hand.value >= 17:
                while player_hand.value < 20:
                    hit_or_stand(deck, player_hand)
                    show_all(player_hand, dealer_hand)
                    time.sleep(3)
            else:
                pass
        else:
            if dealer_hand.value < 17:
                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)
                    show_all(player_hand, dealer_hand)
                    time.sleep(3)

        #time.sleep(3)
        #show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            player_win, dealer_win = dealer_busts(player_hand, dealer_hand, player_chips, player_win, dealer_win)
        elif dealer_hand.value > player_hand.value:
            player_win, dealer_win = dealer_wins(player_hand, dealer_hand, player_chips, player_win, dealer_win)
        elif dealer_hand.value < player_hand.value:
            player_win, dealer_win = player_wins(player_hand, dealer_hand, player_chips, player_win, dealer_win)
        else:
            player_win, dealer_win = push(player_hand, dealer_hand, player_win, dealer_win)
        
        if player_win == True and dealer_win == False:
            print("\nYou WIN:\n£{0}".format(round(player_chips.bet * 1.5)))
            time.sleep(3)
        elif dealer_win == True and player_win == False:
            print("\nYou LOSE:\n£{0}".format(round(player_chips.bet)))
            time.sleep(3)
        else:
            print("\nIt's a TIE")
            time.sleep(3)

        if debt_count > 0:
            print("\nHalf of your winnings goes to your debt.")
            print("\n{0}'s winnings stand at £".format(name) + str(round(player_chips.total)))
            print("Remaining debt owed: £" + str(round((player_chips.debt - (player_chips.debt * 2)))))
            if player_chips.debt >= 0:
                player_chips.total += player_chips.debt
                player_chips.debt = 0
                player_chips.debt_count = 0
                debt_count = 0
                print(
                    "\nYour debt has been wiped clean, and any funds that you may of paid over has now been" \
                    " added to your balance. Good job!\n" \
                    "\nYou now have £{0} avaliable.".format(str(round(player_chips.total)))
                    )
                time.sleep(3)
        else:
            print("\n{0}'s winnings stand at £".format(name) + str(player_chips.total))

        restart, playing = end_of_game()
        if restart > 0 and playing == True:
            continue
        else:
            break
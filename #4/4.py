from random import shuffle
from sys import exit


HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def ShuffleDeck(deck):
    for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
        for num in range(2, 11):
            deck.append((str(num),suit))
        for rank in ['J', 'Q', 'K', 'A']:
            deck.append((rank, suit))
    shuffle(deck)


def ShowCard(symbol,num):
    row1 = '|{}  |\n'.format(num)
    row2 = '| {} |\n'.format(symbol)
    row3 = '|  {}|'.format(num)
    print(row1 + row2 + row3)


def GetBet(maxBet):
    while True:
        bet = input('How much do you bet? (1-{}, or QUIT)'.format(maxBet)).upper().strip()
        if bet.upper() == 'QUIT':
            print('Thanks for playing!')
            exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def ShowHands(dealer, player, showDealerHand):
    if showDealerHand:
        for card in dealer:
            ShowCard(card[0], card[1])
    else:
        ShowCard(dealer[0])
        for card in dealer[1:]:
            ShowCard('#', '#')
    
    for card in player:
        ShowCard(card[0], card[1])

def HandValue(cards):
    point = 0
    for card in cards:
        if card[0] == 'A':
            point += 11
        elif card[0] == 'K' or 'Q' or 'J':
            point += 10
        else:
            point += int(card[0])


def PlayerMove(player, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player) == 2 and money > 0:
            moves.append('(D)ouble down')
        move = input(', '.join(moves) + '> ').upper()
        if move == 'H' or 'S':
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move



def main():
    print('''Blackjack
 Rules:
 Try to get as close to 21 without going over.
 Kings, Queens, and Jacks are worth 10 points.
 Aces are worth 1 or 11 points.
 Cards 2 through 10 are worth their face value.
 (H)it to take another card.
 (S)tand to stop taking cards.
 On your first play, you can (D)ouble down to increase your bet
 but must hit exactly one more time before standing.
 In case of a tie, the bet is returned to the player.
 The dealer stops hitting at 17''')
    deck = []
    ShuffleDeck(deck)
    money = 5000
    while True:

        if money <= 0:
            print("You're broken!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            exit()

        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        print('Money:',money)
        bet = GetBet(money)
        print('Bet: ',bet)


        if HandValue(playerHand) == 21 or (len(playerHand) == 2 and HandValue(playerHand) == 22):
            print('You won ${}'.format(bet))




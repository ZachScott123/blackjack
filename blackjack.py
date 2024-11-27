import random
import db

MONEY = "money.txt"  #global variable for money.txt file

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "Jack", "King", "Ace"]
points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
money = []
deck = []



def createdeck():
    global deck
    deck = []
    for suit in suits:
        for i in range(len(ranks)):
            deck.append([suit, ranks[i], points[i]])
    random.shuffle(deck)
    return deck
#-----------------------------------------------------------------------------
def card_draw():
    return random.choice(deck)
#-----------------------------------------------------------------------------
def card_deal():
    dealer = []
    user = []
    dealer.append(card_draw()) 
    user.append(card_draw())
    both = (dealer, user)
    print(both)
#-----------------------------------------------------------------------------
def print_title():  #function for title_amt
    print("\nWELCOME TO ZACH AND JACOB'S BLACKJACK!")
    print("Blackjack payout is 3:2\n")
#-----------------------------------------------------------------------------
def main(): #call the functions
    print_title()    
    db.money_choice(money, MONEY)
    createdeck()
    #bet_amount()
    card_deal()
#-----------------------------------------------------------------------------
'''def bet_amount():    
    while True:
        try:
            bet_input = int(input("Bet amount: "))
            if bet_input < 5:
                print("bets must be atleast 5")
            elif bet_input > 1000:
                print("bets must not be greater than 1000")'''
            
if __name__ == "__main__":
    main()
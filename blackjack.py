import random
import db

MONEY = "money.txt"  #global variable for money.txt file

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "Jack", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
dealer_points = []
user_points = []
money = []
deck = []




def createdeck():
    global deck
    deck = []
    for suit in suits:
        for i in range(len(ranks)):
            deck.append([ranks[i], suit, values[i]])
        random.shuffle(deck)
    return deck
#-----------------------------------------------------------------------------
def card_draw():
    return deck.pop()
#-----------------------------------------------------------------------------
def blackjack():

    print("\nDEALER'S SHOW CARD:")
    dealer_hand = [card_draw()]
    for card in dealer_hand:
        print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
        dealer_points.append(dealer_hand[0][2])

    print("\nYOUR CARDS:")
    user_hand = [[card_draw()], [card_draw()]]
    for card in user_hand:
        print(f"{card[0][0]} of {card[0][1]}")
        user_points.append(card[0][2])

    print(f"\nDealer points: {sum(dealer_points)}")
    print(f"Your points: {sum(user_points)}")
    
#-----------------------------------------------------------------------------
def print_title():  #function for title
    print("\nWELCOME TO ZACH AND JACOB'S BLACKJACK!")
    print("Blackjack payout is 3:2\n")
#-----------------------------------------------------------------------------
def main(): #call the functions
    print_title()
    db.money_choice(money, MONEY)
    createdeck()
    blackjack()
    buy_chips()
    #bet_amount()
    #blackjack()
#-----------------------------------------------------------------------------
def bet_amount():    
    while True:
        try:
            bet_input = int(input("Bet amount: "))
            if bet_input < 5:
                print("bets must be atleast 5")
            elif bet_input > 1000:
                print("bets must not be greater than 1000")
            elif bet_input > int(money[0]):
                print("bets cannot be higher than the users chips")
            else:
                break
        except ValueError:
            print("error: bet amount must be a valid integer")
#-----------------------------------------------------------------------------           
def buy_chips():
    try:
        for item in money:
            user_amount = int(item)
        while user_amount < 5:
            chips_choice = input("would you like to buy more chips? (y/n): ").lower()
            if chips_choice != "y":
                break
            else:
                with open(MONEY, "w") as file:
                    file.write("100")
                    break
    except ValueError:
        print("error")



  

            

    

if __name__ == "__main__":
    main()
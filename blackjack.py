import random
import db

MONEY = "money.txt"  # Global variable for the file that stores the user's money/chip balance.

# Define the components of a standard deck of cards.
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "Jack", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Card values correspond to ranks.

# Global variables for tracking game state.
dealer_points = []  # Points for dealer's hand.
user_points = []  # Points for user's hand.
money = []  # Tracks the user's money.
deck = []  # The deck of cards in play.
bet = 0  # The user's bet amount.
game = 1  # Game state flag (1 = active, 0 = ended).

#-----------------------------------------------------------------------------
def line():
    # Prints a separator line for better readability in output.
    print("\n-------------------------------")

#-----------------------------------------------------------------------------
def reset():
    # Resets the global variables to start a new game session.
    global suits, ranks, values, dealer_points, user_points, money, deck, bet, game
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "Jack", "King", "Ace"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    dealer_points.clear()
    user_points.clear()
    money = []
    deck.clear()
    bet = 0
    game = 1

#-----------------------------------------------------------------------------
def createdeck():
    # Creates and shuffles a new deck of cards.
    global deck
    deck = []
    for suit in suits:
        for i in range(len(ranks)):
            deck.append([ranks[i], suit, values[i]])
        random.shuffle(deck)
    return deck

#-----------------------------------------------------------------------------
def card_draw():
    # Draws a card from the deck (removes the last card).
    return deck.pop()

def show_points():
    # Displays the current points of the user and dealer.
    print(f"\nYOUR POINTS: {sum(user_points)}")
    print(f"DEALER'S POINTS: {sum(dealer_points)}")

#-----------------------------------------------------------------------------
def check_points():
    # Checks if either the user or dealer has exceeded 17 points to determine a win/loss.
    global game
    if sum(dealer_points) > 17:
        show_points()
        print("\nDealer busted. You win!")
        game = 0
        win = money[0] + (1.5 * bet)
        with open(MONEY, 'w') as file:
            file.write(str(win))
    elif sum(user_points) > 17:
        show_points()
        print("\nYou busted. Dealer wins!")
        game = 0
        loss = money[0] - bet
        with open(MONEY, 'w') as file:
            file.write(str(loss))

#-----------------------------------------------------------------------------
def blackjack():
    # Core function for managing a round of blackjack.
    global game
    while game == 1:
        db.money_choice(money, MONEY)  # Load money from the file.
        if sum(money) < 4:
            with open(MONEY, "w") as file:
                file.write("100")
                money.clear()
                money.append(100)
                print(f"\nRefreshed you with {money[0]} chips, on the house!")
        bet_amount()  # Prompt user to place a bet.

        line()
        round = 1
        print(f"\t-= Round {round} =-")
        
        # Dealer draws one card.
        print("\nDEALER'S SHOW CARD:")
        dealer_hand = [[card_draw()]]
        for card in dealer_hand:
            print(f"- {card[0][0]} of {card[0][1]}")
            dealer_points.append(card[0][2])
        print(f"Dealer points: {sum(dealer_points)}")

        # User draws two cards.
        print("\nYOUR CARDS:")
        user_hand = [[card_draw()], [card_draw()]]
        for card in user_hand:
            print(f"- {card[0][0]} of {card[0][1]}")
            user_points.append(card[0][2])
        print(f"Your points: {sum(user_points)}")
        check_points()  # Check if there's an immediate win/loss.

        while game == 1:
            # Game continues until the user stands or a win/loss occurs.
            try:
                choice = input("\nHit or stand? (hit/stand): ").lower()

                if choice == "hit":
                    # User draws another card.
                    line()
                    round += 1
                    print(f"\t-= Round {round} =-")
                    user_hand.append([card_draw()])
                    user_points.clear()
                    for card in user_hand:
                        print(f"- {card[0][0]} of {card[0][1]}")
                        user_points.append(card[0][2])
                    print(f"Your points: {sum(user_points)}")
                    check_points()
                elif choice == "stand":
                    # Dealer draws until they reach 17 points.
                    while sum(dealer_points) < 17:
                        dealer_hand.append([card_draw()])
                        dealer_points.clear()
                        for card in dealer_hand:
                            dealer_points.append(card[0][2])
                    show_points()
                    if sum(dealer_points) > 21 or sum(user_points) > sum(dealer_points):
                        print("YOU WIN - You had more points.")
                        win = money[0] + (1.5 * bet)
                        with open(MONEY, 'w') as file:
                            file.write(str(win))
                    else:
                        print("YOU LOST - Dealer had more points.")
                        loss = money[0] - bet
                        with open(MONEY, 'w') as file:
                            file.write(str(loss))
                    game = 0
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Please enter 'hit' or 'stand'.")
            except Exception as e:
                print((e), e)

        # Ask the user if they want to play again.
        if game == 0:
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again == 'y':
                if sum(money) < 4:
                    with open(MONEY, "w") as file:
                        file.write("100")
                        print("Here's more chips")
                reset()  # Reset the game state.
                main()
                line()
                break
            elif play_again == 'n':
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid input.")

#-----------------------------------------------------------------------------
def print_title():
    # Displays the game title and rules.
    print("\nWELCOME TO ZACH AND JACOB'S BLACKJACK!")
    print("Blackjack payout is 3:2\n")

#-----------------------------------------------------------------------------
def bet_amount():    
    # Prompts the user to place a bet and validates the input.
    global bet
    while True:
        try:
            bet_input = float(input(f"\nBet amount [{money[0]}]: "))
            bet = bet_input
            if bet_input < 5:
                print("Bets must be at least 5.")
            elif bet_input > 1000:
                print("Bets must not exceed 1000.")
            elif bet_input > money[0]:
                print("Bets cannot exceed your available chips.")
            else:
                break
        except ValueError:
            print("Error: Bet amount must be a valid number.")

#-----------------------------------------------------------------------------
def buy_chips():
    # Allows the user to buy more chips if their balance is too low.
    try:
        for item in money:
            user_amount = int(item)
        while user_amount < 5:
            chips_choice = input("Would you like to buy more chips? (y/n): ").lower()
            if chips_choice != "y":
                break
            else:
                with open(MONEY, "w") as file:
                    file.write("100")
                    break
    except ValueError:
        print("Error, invalid input.")

#-----------------------------------------------------------------------------
def main():
    # Main function that starts the game.
    print_title()
    createdeck()
    blackjack()
    buy_chips()

#-----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


MONEY = "money.txt"  #global variable for money.txt file

def print_title():  #function for title
    print("\nWELCOME TO ZACH AND JACOB'S BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def money_choice(): #function to prompt user about money at the start
    try:
        with open(MONEY):
            pass
        while True: #while loop for input
            
            create = int(input("1 - Start with previous balance\n2 - Start with default balance: [100]\n\t  ( 1 / 2 )\n\t      "))
            if create == 1:                                   #---Depending on what input given, create or reuse money.txt
                print("\nStarting with previous balance.")
                break
            elif create == 2:
                print("\nStarting with default balance.")
                with open(MONEY, "w") as file:
                    file.write("100")
                    break
            else:
                print("Invalid input.")
    except FileNotFoundError:   #if file not found create new and give user 100 balance
        print(f"Could not find ({MONEY}) file!")
        print("Player starting balance: 100")
        with open(MONEY, "w") as file:
            file.write("100")

def main(): #call the functions
    print_title()
    money_choice()

if __name__ == "__main__":
    main()
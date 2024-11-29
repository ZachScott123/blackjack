def money_choice(money, MONEY): #function to prompt user about money at the start
    try:
        
        with open(MONEY, newline="") as file:
            for line in file:

                while True: #while loop for input

                    try:
                        create = int(input(f"\n1 - Start with previous balance: [{line}]\n2 - Start with default balance: [100]\n\t  ( 1 / 2 )\n\t      "))

                        if create == 1:                                   #---Depending on what input given, create or reuse money.txt
                            print("\nStarting with previous balance.")
                            money.append(line)
                            break

                        elif create == 2:
                            print("\nStarting with default balance.")
                            with open(MONEY, "w") as file:
                                file.write("100")
                                money.append(line)
                                break
                            
                        else:
                            print("Invalid input.")
                    except ValueError:
                        print("Invalid input. Please enter 1 or 2.")
                        continue
                    except Exception as e:
                        print((e), e)

    except FileNotFoundError:   #if file not found create new and give user 100 balance
        print(f"Could not find ({MONEY}) file!")
        print("Player starting balance: 100")
        with open(MONEY, "w") as file:
            file.write("100")
    except Exception as e:
        print((e), e)
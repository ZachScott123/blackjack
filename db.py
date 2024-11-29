def money_choice(money, MONEY): # Function to prompt user about money at the start
    try:
        
        with open(MONEY, newline="") as file:
            for line in file:

                while True: # While loop for input
                    create = 0
                    try:
                        create = int(input(f"\n1 - Start with previous balance: [{line}]\n2 - Start with default balance: [100]\n\t  ( 1 / 2 )\n\t      "))

                        if create == 1:                                   #---Depending on what input given, create or reuse money.txt
                            print("\nStarting with previous balance.")
                            money.append(float(line))   # Float value so that error doesn't occur when selecting input
                            break

                        elif create == 2:
                            print("\nStarting with default balance.")
                            with open(MONEY, "w") as file:
                                file.write("100")
                                money.append(float(line))
                                break
                            
                        else:
                            print("Invalid input.")
                            continue
                        return create
                    except ValueError:
                        print("Invalid input. Please enter 1 or 2.")
                        continue
                    except Exception as e:
                        print((e), e)

    except FileNotFoundError:   # If file not found create new and give user 100 balance
        print(f"Could not find ({MONEY}) file!")
        print("Player starting balance: 100")
        with open(MONEY, "w") as file:
            file.write("100")
    except Exception as e:
        print((e), e)
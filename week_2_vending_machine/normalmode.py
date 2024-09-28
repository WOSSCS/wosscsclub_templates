def vending_machine():
    # Step 2: Define a dictionary for drink prices
    # Use drink numbers as keys (e.g., "1" for water) and their prices as values
    
    prices = {
        "1": 1.00,  # Water
        "2": 1.50,  # Soda
        "3": 2.00   # Coffee
    }

    # Step 3: Create a function to display the menu
    # This function should print out the options available to the user

    def display_menu():
        # Print the menu (water, soda, coffee, and the option to quit)
        pass  # <-- Replace with actual print statements for the menu

    # Step 4: Set up the main loop
    # This loop should keep the vending machine running until the user selects "Quit"

    while True:
        # Call the function to display the menu
        # Ask the user to input their drink choice (1, 2, 3 for drinks, 4 to quit)
        
        choice = input("Please select a drink (1-4): ")

        # Step 5: Add a condition to check if the user wants to quit (input is "4")
        if choice == "4":
            print("Thank you for using the vending machine. Goodbye!")
            break  # Exit the loop if the user chooses to quit

        # Step 6: Check if the user's choice is valid (i.e., it must be one of the available drinks)
        # Hint: Use an if-else or elif structure to handle invalid choices
        if choice not in prices:
            print("Invalid selection. Please try again.")
            continue  # Go back to the start of the loop if the input is invalid

        # Step 7: Retrieve the price of the selected drink from the dictionary
        drink_price = prices[choice]
        
        # Step 8: Ask the user to input the amount of money inserted
        # Convert the input to a float since it will be a decimal value
        money_inserted = float(input(f"The price is ${drink_price:.2f}. Please insert money: $"))

        # Step 9: Compare the money inserted with the drink price
        if money_inserted >= drink_price:
            # Step 10: If the money is enough, calculate and display the change (money_inserted - drink_price)
            # Print a message to dispense the drink and show the change
            
            pass  # <-- Replace with code to calculate and print the change

        else:
            # Step 11: If the money is not enough, enter a loop to ask for more money
            while money_inserted < drink_price:
                # Ask the user to insert more money
                # Add the new amount to the money_inserted total
                pass  # <-- Replace with code to ask for more money and update total
        
        # After dispensing the drink or receiving enough money, ask if the user wants another drink
        print("\nWould you like another drink?")

# Call the vending machine function to start the program
vending_machine()


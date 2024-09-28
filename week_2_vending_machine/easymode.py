# Define drink prices
prices = {
    "1": 1.00,  # Water
    "2": 1.50,  # Soda
    "3": 2.00   # Coffee
}

# Display the menu (students need to complete this)
print("1: Water ($1.00)")
print("2: Soda ($1.50)")
print("3: Coffee ($2.00)")
print("4: Quit")

# Main program
while True:
    # Get user choice for the drink
    choice = input("Please select a drink (1-4): ")

    # If the user selects "4", quit the program
    if choice == "4":
        print("")
        #stop the breaks!!

    # Check if the choice is valid
    if choice not in prices:
        print("Invalid ...")
        #continue the breaks!!

    # Get the price of the selected drink
    drink_price = prices[choice]

    # Ask the user to input money (students need to handle the logic here)
    money_inserted = float(input("The price is " + str(drink_price) + ". Please insert money: $"))

    # Check if enough money was inserted
    if money_inserted >= drink_price:
        # Calculate the change (students should add the code for this)
        pass  # <-- Students calculate and print the change here
    else:
        # Ask for more money until enough is inserted (students should handle this)
        pass  # <-- Students add the logic to ask for more money here

    # Ask if the user wants another drink (optional for students to implement)
    pass

inserted_money = 0 #setting up some variables so you can't see the ugly red squiggly lines
price = 0
#Define a dictionary of prices for drinks:
    #"1" corresponds to Water ($1.00)
    #"2" corresponds to Soda ($1.50)
    #"3" corresponds to Coffee ($2.00)

#Define a function to display the menu:
    print(
        #1: Water ($1.00)"
        #2: Soda ($1.50)"
        #3: Coffee ($2.00)"
        #4: Quit"
    )

#Start a loop that repeats until the user decides to quit:
    #display the menu

    #Ask the user to select a drink (1-4)

    if #the user selects "4" :
        print(a goodbye message) # ↑ don't forget to add a ":" after the if statement!
        #Exit the loop

    if #the user selects an invalid option (anything not in the price list):
        print ("an error message")

    if #the selection is valid:
        #Get the price of the selected drink

        input ("Ask the user to insert money") #don't forget to convert the input to a float!

        if inserted_money == price or inserted_money > price:
            #Calculate the change (inserted money - price)
            print ("a formated string to dispense the drink and show the change")

        elif inserted_money < price:
            #Start a while loop to ask for more money until the total inserted is enough:
                #Ask for more money (inserted amount should keep adding to the total)
                total_money = inserted_money + input("Ask the user to insert more money") #don't forget to convert the input to a float!
                if total_money >= price:
                    #Calculate the change
                    print ("a formated string to dispense the drink and show the change")

# Start the program
# function here
# PROGRAM:     Pgm U4 Fuel
# AUTHOR:      Robert Depweg
# DESCRIPTION: This program calculates the total cost of filling up 
#              their vehicle with a certain type of fuel.
# INPUT:       The type of fuel, and if the user would like to fill
#              up to a whole tank.
# OUTPUT:      What kind of fuel was chosen, how many gallons were
#              needed, and the total cost.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\033c")
import sys
import random

# - - - - -  - - - - - - - - - - - - - - - - - - - - - - CONSTANT DECLARATIONS

TANK_CAPACITY:int = 55                # Gallons of gas tank will hold
UNLEADED_PRICE:float = 3.75           # Price of unleaded fuel
SUPER_UNLEADED_PRICE:float = 3.95     # Price of super unleaded fuel
DIESEL_PRICE:float = 4.15             # Price of diesel fuel
DIESEL_PREMIUM_PRICE:float = 4.25     # Price of unleaded fuel
# - - - - - - - - - - - - - - - - - - - - - - - - - - - VARIABLE INITIALIZATION

current_fuel_level:int = 0            # Random number generated 0-55
fuel_choice:str = ''                  # User fuel choice from menu
fuel_descr:str = ''                   # Description of fuel chosen
price_per_gal:float = 0.0             # Price per gallon from menu
full_tank:str = ''                    # Full tank fill indicator
quantity_needed:int = 0               # Amount of fuel to put in tank
cost:float = 0.0                      # Cost of fuel purchased

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - INPUT
# Generate a random # of gallons to start with
current_fuel_level = random.randint(0,55)


print(f"You have {current_fuel_level} gallons left in your tank.\n")

# Display Menu
print(" ---- Our Prices ----")
print(f"A - Unleaded: ${UNLEADED_PRICE} per gallon.")
print(f"B - Super Unleaded: ${SUPER_UNLEADED_PRICE} per gallon.")
print(f"C - Diesel: ${DIESEL_PRICE} per gallon.")
print(f"D - Diesel Premium: ${DIESEL_PREMIUM_PRICE} per gallon.")
print()

# Ask user to enter menu option for fuel choice
fuel_choice = input(f'What fuel do you need? ')

# Assign price_per_gallon and fuel description
# based on user fuel choice
if fuel_choice == 'A':
    price_per_gal = UNLEADED_PRICE
    fuel_descr = "Unleaded"
elif fuel_choice == 'B':
    price_per_gal = SUPER_UNLEADED_PRICE
    fuel_descr = "Super Unleaded"
elif fuel_choice == 'C':
    price_per_gal = DIESEL_PRICE
    fuel_descr = "Diesel"
elif fuel_choice == 'D':
    price_per_gal = DIESEL_PREMIUM_PRICE
    fuel_descr = "Diesel Premium"

# If the user enters an invalid menu item the program execution ends.
else:
    sys.exit('\nInvalid Menu Option.')

# Ask user if they would like to fill up their tank.
full_tank = input(f'Would you like to fill up to a full tank? y/n ')

# Calculate quantity of gallons needed
if full_tank == 'y':
    quantity_needed = TANK_CAPACITY - current_fuel_level
    # Get number of gallons user want to put in tank
else:
    quantity_needed = int(input('How many gallons do you need? '))
    # Check to make sure tank does not overflow
    if quantity_needed > TANK_CAPACITY:
        quantity_needed = TANK_CAPACITY - current_fuel_level

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -CALCULATIONS
# The cost of the gallons times the quantity of fuel needed
# gives the total cost
cost = price_per_gal * quantity_needed

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -OUTPUT
# Prints the fuel choice, the quantity, and the total cost
print(f"\nFuel Choice: {fuel_descr}")
print(f"Quantity: {quantity_needed} gallons.")
print(f"Total Cost: ${cost:.2f}")

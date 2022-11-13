# Import random module to generate random spins
import random


# Declare a global variable to keep the max number of lines to bet, max and min allowable bet on a constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Declare values for number of rows and columns to display in a spin
ROWS = 3
COLS = 3

symbols = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Reread this code once more
def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = list()
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_spin(cols, rows, symbols):
    """
    
    """
    all_symbols = list()
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = list()
    for _ in range(cols):
        column = list()
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)

        columns.append(column)
    
    return columns

# Tricky Code this One
def print_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end ="")
        
        print()

def deposit():
    """
    Gets the deposit from the user: How much they want to gamble.
    """

    # To keep asking for an input until we get valid input: Integer > 0
    while True:             
        amount = input("How much do you want to deposit? $")
        
        # Check if input has digits only to convert into a valid number
        if amount.isdigit(): 
        
            # Convert the amount to an integer type
            amount = int(amount)
        
            # Check if amount is a positive number as deposit cannot be negative
            if amount > 0:
                # Break the loop if true
                break
        
            # If amount is negative or zero
            # print a prompt to let the user know of the valid input
            else:
                print("Deposit should be greater than zero.")
        
        # If the input is not valid as in doesnt have only digits
        # print a prompt to let user know of valid entries
        else:
            print("Please enter a valid number.")
    
    # Return the amount from the function as an output
    return amount

def get_lines_to_bet():
    f"""
    Gets the number of lines the user wants to bet on.
    Minimum Lines: 1
    Maximum Lines: {MAX_LINES}
    """

    # To keep asking for an input until we get valid input: 1 <= Integer <= MAX_LINES
    while True:             
        lines = input("How many lines do you want to bet on? (1-" + str(MAX_LINES) + ") ")
        
        # Check if input has digits only to convert into a valid number
        if lines.isdigit(): 
        
            # Convert the lines to an integer type
            lines = int(lines)
        
            # Check if lines is within the allowed limits
            if 1 <= lines <= MAX_LINES:
                # Break the loop if true
                break
        
            # If lines is out of bounds
            # print a prompt to let the user know of the valid input
            else:
                print(f"Number of lines should be between 1 and {MAX_LINES}.")
        
        # If the input is not valid as in doesnt have only digits
        # print a prompt to let user know of valid entries
        else:
            print("Please enter a valid number.")
    
    # Return the lines from the function as an output
    return lines

def get_bet():
    """
    Gets the amount of a single bet from the user.
    """

    # To keep asking for an input until we get valid input: MIN_BET <= Integer <= MAX_BET 
    while True:             
        amount = input("How much do you want to bet on each line? $")
        
        # Check if input has digits only to convert into a valid number
        if amount.isdigit(): 
        
            # Convert the amount to an integer type
            amount = int(amount)
        
            # Check if amount is a valid bet amount
            if MIN_BET <= amount <= MAX_BET:
                # Break the loop if true
                break
        
            # If amount is outside bounds
            # print a prompt to let the user know of the valid input
            else:
                print(f"Deposit should be between {MIN_BET} and {MAX_BET}.")
        
        # If the input is not valid as in doesnt have only digits
        # print a prompt to let user know of valid entries
        else:
            print("Please enter a valid number.")
    
    # Return the amount from the function as an output
    return amount

def spin(balance):
        
    # Check if the total bet is within balance amount
    while True:
        lines = get_lines_to_bet()
        bet = get_bet()
        total_bet = lines * bet

        # If balance less than total bet, display balance.
        if total_bet > balance:
            print(f"You do not have enough to bet. Your balance is ${balance}. You are trying to bet ${total_bet}")
        # If balance more than or equal to total bet, break the loop
        else:
            break
        
    print(f"""\nYou are betting ${bet} each on {lines} lines.\nYour total bet is ${total_bet}\n""") 
    
    slots = get_spin(COLS, ROWS, symbols)
    print_spin(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines: ", *winning_lines)
    
    return winnings - total_bet

def main():
    balance =  deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        if balance <= 0:
            print(f"Sorry. You have run out of deposit.")
            break

    print(f"You are left with ${balance}.")


main()

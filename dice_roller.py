import random
import re
def roll_dice(die, quantity, modifier=0): 
    rolls = []
    for _ in range(int(quantity)):
        roll = random.randint(1, int(die))
        rolls.append(roll)
    total = sum(rolls) + modifier

    #Highlight crits
    formatted_rolls = []
    for r in rolls:
        if r == die: # Max roll (crit success in D&D)
            formatted_rolls.append(f"[{r}]") # brackets for crits
        elif r == 1: # Min roll (crit fail)
            formatted_rolls.append(f"({r}") # parentheses for fails
        else: 
            formatted_rolls.append(str(r))

    print(f"\nRolling {quantity}d{die}{'+' + str(modifier) if modifier > 0 else ('-' + str(abs(modifier)) if modifier < 0 else '')}:")
    print(f"Results: {', '.join(formatted_rolls)}")

    if modifier != 0: 
        # You rolled [x,y,x] + modifier if it's greater that or equal to 0 otherwise it will print nothing and the total
        print(f"You rolled: {sum(rolls)} {'+' if modifier >= 0 else ''} = {total}")
    else: 
        print(f"Sum: {total}")

    return total

# Get Valid Dice
def get_valid_die():
    valid_dice = [4, 6, 8, 10, 12, 20, 100]

    while True:
        die_input = input("\nWhich Die?:")
        if die_input.lower() == 'q':
            return None
        # Checks if the user input starts with a 'd' and strips it
        if die_input.startswith('d'):
            die_input = die_input[1:]
        
        # Try to convert to int and validate
        try: 
            die = int(die_input)
            if die in valid_dice:
                return die
            else:
                print(f"Sorry, d{die} isn't a standard die. Choose from: {', '.join('d' + str(d) for d in valid_dice)}")
        except ValueError:
            print("Sadly that's not a die. Try again!")

# Get a valid number of die from the user
# def get_valid_count():
#     while True:
#         count_input = input("How many dice? (1-10) or 'q' to quit: ")
        
#         if count_input.lower == 'q':
#             return None
        
#         try:
#             count = int(count_input)
#             if 1 <= count <= 10:
#                 return count
#             else:
#                 print("Please enter a number between 1 and 10")
#         except ValueError:
#             print("That is an invalid number, please try again")

# Parses dice notation
def parse_dice_notation(notation):
    """ Parse dice notation (i.e. d20, 2d6+5), 
    returns (num_dice, die_size, modifier) or none if invalid"""
    pattern = r'^(\d*)d(\d+)([+-]\d+)?$'
    match = re.match(pattern, notation.lower().replace(' ', ''))

    if not match:
        return None
    
    # maps the variables to the notation
    num_dice = int(match.group(1)) if match.group(1) else 1
    die_size = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    return (num_dice, die_size, modifier)
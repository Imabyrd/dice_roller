import dice_roller as dc
# A dice roller for dnd
# returns the die rolls, and sum of the rolls
    # Take in how many die are being rolled
    # parses input for die number

def main():
    print("|======================== DICE ROLLER ========================|")
    print("|======================= _INSTRUCTION_ =======================|")
    print("| 1. Input the size of the die you'd like to roll.            |")
    print("|    ex. 2d20, d6, 3d8+5, 1d20-2.                             |")
    print("| 1. Press 'q' to quit.                                       |")
    print("|______________ _______________________________ ______________|")
    print("|______________ _Select a die size to continue_ ______________|")

    while True:
        notation = input("Enter Dice roll: \n")
        
        if notation == 'q':
            break
        result = dc.parse_dice_notation(notation)
        
        if result is None:
            print("Invalid format! Use notation like this: 2d20, d6+3, 1d8-1")
            continue

        num_dice, die_size, modifier = result
        dc.roll_dice(die_size, num_dice, modifier)
    
    print("Thanks for rolling!")

if __name__ == '__main__':
    main()

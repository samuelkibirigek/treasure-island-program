print("Welcome to the Treasure Island. \nYour mission is to find the treasure.")

direction = input('You\'re at a crossroads, which way do you go? Type "Left" or "Right"?\n').lower()

if direction == "right":
    print("Game over, should have gone left!")

elif direction == "left":
    island = input("You've come to a lake. There is an Island in the middle of the lake. "
                   "Type 'wait' to wait for boat or 'swim' to swim across.\n").lower()

    if island == "swim":
        print("Game over! You got eaten by a trout!")

    elif island == "wait":
        door = input("You arrive at the Island unharmed. There is a house with three doors"
                     " red, blue and yellow. Which door will you enter?\n").lower()

        if door == "yellow":
            print("You win!")

        elif door == "red" or door == "blue":
            print("Game over! Sorry... wrong door.")

        else:
            print("Invalid Input!")

    else:
        print("Invalid Input!")

else:
    print("Invalid Input!")



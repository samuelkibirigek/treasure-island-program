print("Welcome to the Treasure Island. \nYour mission is to find the treasure.")

direction = input("Left or Right?").lower()

if direction == "right":
    print("Game over, should have gone left!")

elif direction == "left":
    island = input("Swim or wait?").lower()

    if island == "swim":
        print("Game over! You got eaten!")

    elif island == "wait":
        door = input("Which door! Red, blue or yellow?").lower()

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



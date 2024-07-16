import random as r
choices = ["r", "p", "s"]
def game():
    p_choice = str(input("Enter you choice 'r' for 'rock', 'p' for 'paper' and 's' for 'scissors' : "))
    c_choice = choices[r.randrange(0, 3)]
    if (p_choice in choices):
        # Condition for Winning
        if (p_choice == "r" and c_choice == "s" or p_choice == "p" and c_choice == "r" or p_choice == "s" and c_choice == "p"):
            print("You win")
            return
        # Condition for Winning
        elif (p_choice == "r" and c_choice == "p" or p_choice == "p" and c_choice == "s" or p_choice == "s" and c_choice == "r"):
            print("You lose")
            return
    else:
        print("Invalid!")
        game()

if __name__ == "__main__":
    while True:
        ask = str(input("Would you like to play the game? (Type 'y' for 'yes' and 'n' for 'no')"))
        if (ask == "y"):
            game()
        elif (ask == "n"):
            quit()
        else:
            print("Invalid")
def start_game():
    print("Welcome to the Dungeon Adventure!")
    print("You find yourself standing at the entrance of a dark dungeon.")
    print("Do you want to enter the dungeon? (yes/no)")

    choice = input("> ").lower()

    if choice == "yes":
        enter_dungeon()
    elif choice == "no":
        print("You decide to leave. Maybe next time.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        start_game()

def enter_dungeon():
    print("\nYou step into the dungeon. The door slams shut behind you.")
    print("There are two paths ahead: one to the left and one to the right.")
    print("Which path will you take? (left/right)")

    choice = input("> ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        enter_dungeon()

def left_path():
    print("\nYou walk down the left path and encounter a fearsome dragon!")
    print("Do you want to fight the dragon or run away? (fight/run)")

    choice = input("> ").lower()

    if choice == "fight":
        print("You bravely charge at the dragon, but it breathes fire and you are defeated.")
        print("Game Over!")
    elif choice == "run":
        print("You turn around and run back to the entrance, escaping the dragon.")
        start_game()
    else:
        print("Invalid choice. Please type 'fight' or 'run'.")
        left_path()

def right_path():
    print("\nYou take the right path and find a treasure chest.")
    print("Do you want to open the chest? (yes/no)")

    choice = input("> ").lower()

    if choice == "yes":
        print("You open the chest and find a pile of gold! You win!")
    elif choice == "no":
        print("You leave the chest alone and return to the entrance.")
        start_game()
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        right_path()

# Start the game
start_game()
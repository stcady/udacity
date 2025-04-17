import random
import time


# Helper function to print messages with a delay
def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


# Helper function to handle user choices
def choice_menu(option_list, question):
    options = []
    for i, option in enumerate(option_list):
        print_pause(f"Enter [{i + 1}] {option}")
        options.append(str(i + 1))
    if question != "":
        print_pause(question)
    return validate_choice(options)


# Helper function to validate user input
def validate_choice(valid_choices):
    valid_options = ", ".join(valid_choices)
    user_input = input(f"Please enter ({valid_options}): ").strip().lower()
    while user_input not in valid_choices:
        user_input = validate_choice(valid_choices)
    return user_input


# Game function to introduce the game and the monster
def intro():
    print_pause("WELCOME TO THE GAME!")
    monster = random.choice(["ZOMBIES 🧟", "GHOSTS 👻", "VAMPIRES 🧛",
                             "DEMONS 😈", "BEASTS 👹", "ALIENS 👽"])
    print_pause("You are in a maze and can barley see.")
    print_pause(f"The maze is full of {monster}. "
                "You can hear them making noises...")
    print_pause(f"OBJECTIVE: Exit the house "
                "without encountering the {monster}.")
    return monster


# Game function start at the spawn point
def start_game(monster):
    print_pause("\nYou're presently in a large empty room. "
                "There are three options:")
    choice = choice_menu(
        ["to go down the hall.",
         "to go through the door ahead.",
         "to go down the stairs."],
        "Where do you want to go?"
        )
    game_won = False
    if choice == '1':
        game_won = random.choice([monster_encounter, empty_room])(monster)
    elif choice == '2':
        game_won = random.choice([monster_encounter, empty_room])(monster)
    elif choice == '3':
        game_won = random.choice([monster_encounter, empty_room])(monster)
    if game_won:
        print_pause("\nCONGRATS! You won the game! 🎖️")
    else:
        print_pause("\nGAME OVER! You lost the game. ☠️")


# Game function to handle entering the room
def enter_room():
    print_pause("\nYou slowly and nervously enter the next area...")


# Game function to handle monster encounter
def monster_encounter(monster):
    enter_room()
    print_pause("It's too dark to see clearly...")
    print_pause("Suddenly, a figure appears behind you...")
    print_pause(f"The {monster} found you! You are trapped! 😱")
    return False


# Game function to handle the empty room
def empty_room(monster):
    enter_room()
    print_pause("It is empty 😅.")
    return next_move(monster)


# Game function to handle the exit room
def exit_room(monster):
    enter_room()
    print_pause(f"You found the exit and escaped the"
                "maze safely without encountering any {monster}!")
    return True


# Game function to handle the next move
def next_move(monster):
    print_pause("\nYou have two choices:")
    choice = choice_menu(
        ["to go through the door ahead.",
         "to go down the stairs."],
        "Where do you want to go?"
        )
    if choice == '1':
        return random.choice([monster_encounter,
                              exit_room,
                              empty_room])(monster)
    elif choice == '2':
        return random.choice([monster_encounter,
                              exit_room,
                              empty_room])(monster)
    else:
        print_pause("That’s not a valid choice.")
        return next_move()


# Game function to ask if the player wants to play again
def play_again():
    print_pause("\nDo you want to play again?")
    play_again = choice_menu(["YES", "NO"], "")
    if play_again == "1":
        print("\nRestarting the game in 5 seconds... 🙌\n")
        time.sleep(5)
        play_game()
    elif play_again == "2":
        print("\nThanks for playing! 👋")


# Game function to start the game
def play_game():
    monster = intro()
    start_game(monster)
    play_again()


# Run the game
play_game()

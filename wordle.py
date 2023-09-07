import emoji
from rich.console import Console
from rich.text import Text
from rich.emoji import Emoji
from rich import print

import random
import sys

# constants
console = Console()

style_correct_spot = "bold white on green"
style_correct_letter = "bold white on yellow"
style_incorrect = "white on #666666"

# DISPLAY functions (menu, text, game board)

def display_menu():
    print()
    console.rule(":hibiscus: Wordle :hibiscus:")
    print("[green]1. Play game[/] :game_die:")
    print("[cyan]2. Display rules[/] :page_facing_up:")
    print("[red]3. Exit game[/] :thumbsdown:\n")
    
    choice = input("What would you like to do? (1-3): ")

    if choice == "1":
        play()
    elif choice == "2":
        display_rules()
    elif choice == "3":
        exit()
    else:
        invalid_response = Text("Invalid Response. Choose 1 (play), 2 (rules), or 3 (exit).")
        invalid_response.stylize("bold red")
        console.print(invalid_response)

        display_menu()

def display_board(attempt=1):
    console.rule(f"Guess {attempt}")
    
def display_rules():
    console.rule(":page_facing_up: How to Play :page_facing_up:")

    print("\nGuess the word in 6 tries.\n")

    print("The color of the tiles will change to show how close your guess was to the word.\n")

    print("- [black on green]Green[/] indicates that the letter is in the word and in the correct spot.")

    print("- [black on yellow]Yellow[/] indicates that the letter is in the word but in the wrong spot.")

    print("- [black on gray]Gray[/] indicates that the letter is not in the word.\n")

    input("Press enter/return to continue...\n")
    display_menu()

def exit():
    print("\nExiting...\n")
    sys.exit(0)

def select_word():
    # open words.txt an select random word
    with open("words.txt") as f:
        words = f.readlines()
        word = random.choice(words).strip()
    return word

def play():
    # display_board()

    word = select_word()

    num_guesses = 0

    while num_guesses < 6:
        display_board(num_guesses + 1)
        guess = input("Guess a letter: ")
        num_guesses += 1

        if guess in word:
            print(f"{guess} is in the word!")
        else:
            print(f"{guess} is not in the word!")

def start():
    display_menu()
    

if __name__ == "__main__":
    start()
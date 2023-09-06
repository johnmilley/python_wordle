import emoji
from rich.console import Console
from rich.text import Text

import sys


def display_menu():
    console = Console()
    text = Text("\nWordle\n======")
    text.stylize("bold yellow")

    option_play = Text("1. Play game")
    option_play.stylize("green")

    option_rules = Text("2. Display rules")
    option_rules.stylize("cyan")

    option_exit = Text("3. Exit game\n")
    option_exit.stylize("red")

    console.print(text)
    console.print(option_play)
    console.print(option_rules)
    console.print(option_exit)
    
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
    

def display_rules():
    print("\nhow to play wordle\n")
    input("Press enter/return to continue...")
    display_menu()

def exit():
    print("\nExiting...")
    sys.exit(0)

def play():
    print("play\n")
    display_menu()


def start():
    display_menu()

if __name__ == "__main__":
    start()
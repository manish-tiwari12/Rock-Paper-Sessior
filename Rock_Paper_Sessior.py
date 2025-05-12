import random

emojis = { "r": "🪨", "s": "✂️", "p": "📃" }
choices = ("r", "s", "p")

def get_user_choice():
    while True:
        user_choice = input('Choose One: Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice..!")

def display_choice(user_choice, computer_choice):
    print(f"Your choice: {emojis[user_choice]}")
    print(f"Computer choice: {emojis[computer_choice]}")

def declare_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Game is a Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        print("Congrats..🎉🎉 You Win!")
    else:
        print("You Lose..")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        declare_winner(user_choice, computer_choice)
        should_continue = input("Do you want to continue the game? (y/n): ").lower()
        if should_continue == "n":
            break

play_game()


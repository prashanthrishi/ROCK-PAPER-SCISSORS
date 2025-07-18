import random
from art import rock,paper,scissors

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

        if user_choice < 0 or user_choice > 2:
            print("Invalid input! You typed an invalid number. Please try again (0, 1, or 2).")
            continue
        print("\nYour choice:")
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print("Computer's choice:")
        print(game_images[computer_choice])
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? Type 'yes' or 'no'.\n").lower()
        if play_again != 'yes':
            break

    except ValueError:
        print("Invalid input! Please type a number (0, 1, or 2).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("Thanks for playing!")

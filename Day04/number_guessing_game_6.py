import random

def generate_secret_number():
    return random.randint(1, 20)

# Initial setup
secret_number = generate_secret_number()
debug_mode = False
move_mode = False

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 20.")
print("Commands:")
print("  'x' = quit")
print("  's' = show secret number once")
print("  'd' = toggle debug mode (always show secret)")
print("  'm' = toggle move mode (number shifts after each guess)")
print("  'n' = start a new game with a new number")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number: {secret_number}")

    guess = input("Enter your guess: ")

    # Quit game
    if guess.lower() == 'x':
        print("You chose to quit the game. Goodbye!")
        break

    # Show secret number once
    if guess.lower() == 's':
        print(f"[CHEAT] The secret number is: {secret_number}")
        continue

    # Toggle debug mode
    if guess.lower() == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode is now {'ON' if debug_mode else 'OFF'}.")
        continue

    # Toggle move mode
    if guess.lower() == 'm':
        move_mode = not move_mode
        print(f"Move mode is now {'ON' if move_mode else 'OFF'}.")
        continue

    # Start a new game with new secret number
    if guess.lower() == 'n':
        secret_number = generate_secret_number()
        print("New game started! A new secret number has been chosen.")
        continue

    # Check if input is a valid number
    if not guess.isdigit():
        print("Invalid input. Please enter a number or use one of the commands: x, s, d, m, n.")
        continue

    guess = int(guess)

    # Compare guess
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Congratulations! You guessed the number!")
        secret_number = generate_secret_number()
        print("A new number has been generated. Keep playing!")
        continue

    # Move mode logic: change the number slightly after each guess
    if move_mode:
        shift = random.choice([-2, -1, 0, 1, 2])
        secret_number += shift
        secret_number = max(1, min(20, secret_number))  # Keep within bounds
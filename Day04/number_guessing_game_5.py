import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
debug_mode = False
move_mode = False

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 20.")
print("Commands: 'x' = quit, 's' = show secret once, 'd' = toggle debug mode, 'm' = toggle move mode.")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number: {secret_number}")

    guess = input("Enter your guess: ")

    # Quit game
    if guess.lower() == 'x':
        print("You chose to quit the game. Goodbye!")
        break

    # Cheat: show the secret once
    if guess.lower() == 's':
        print(f"[CHEAT] The secret number is: {secret_number}")
        continue

    # Toggle debug mode
    if guess.lower() == 'd':
        debug_mode = not debug_mode
        status = "ON" if debug_mode else "OFF"
        print(f"Debug mode is now {status}.")
        continue

    # Toggle move mode
    if guess.lower() == 'm':
        move_mode = not move_mode
        status = "ON" if move_mode else "OFF"
        print(f"Move mode is now {status}.")
        continue

    # Validate input
    if not guess.isdigit():
        print("Invalid input. Please enter a number, or use 'x', 's', 'd', or 'm'.")
        continue

    guess = int(guess)

    # Compare guess
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Congratulations! You guessed the number!")
        break

    # If move mode is on, adjust the secret number
    if move_mode:
        change = random.choice([-2, -1, 0, 1, 2])
        secret_number += change
        # Keep the secret number within bounds
        secret_number = max(1, min(20, secret_number))
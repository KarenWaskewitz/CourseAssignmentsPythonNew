import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)
debug_mode = False  # Start with debug mode OFF

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 20.")
print("Commands: 'x' = quit, 's' = show secret once, 'd' = toggle debug mode.")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number: {secret_number}")

    guess = input("Enter your guess: ")

    # Quit the game
    if guess.lower() == 'x':
        print("You chose to quit the game. Goodbye!")
        break

    # Cheat: show the secret number once
    if guess.lower() == 's':
        print(f"[CHEAT] The secret number is: {secret_number}")
        continue

    # Toggle debug mode on/off
    if guess.lower() == 'd':
        debug_mode = not debug_mode  # Flip the debug flag
        status = "ON" if debug_mode else "OFF"
        print(f"Debug mode is now {status}.")
        continue

    # Validate number input
    if not guess.isdigit():
        print("Invalid input. Please enter a number, or use 'x', 's', or 'd'.")
        continue

    # Convert to integer and compare
    guess = int(guess)

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Congratulations! You guessed the number!")
        break
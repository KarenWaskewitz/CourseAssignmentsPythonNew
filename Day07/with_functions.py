import random

def generate_number():
    """Generate a random number between 1 and 20."""
    return random.randint(1, 20)

def get_guess():
    """Prompt the user for a guess and return it as an integer."""
    while True:
        try:
            return int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("Please enter a valid number.")

def give_feedback(guess, number):
    """Return feedback based on the guess."""
    if guess < number:
        return "Sorry, your number is too small."
    elif guess > number:
        return "Sorry, your number is too big."
    else:
        return "correct"

def play_game():
    """Run the number guessing game."""
    number = generate_number()
    print("The computer chose a number between 1 and 20.")
    turns = 0

    while True:
        guess = get_guess()
        turns += 1
        result = give_feedback(guess, number)

        if result == "correct":
            print(f"Congratulations, you are right! It took you {turns} tries.")
            break
        else:
            print(result)

def main():
    """Main function to start the game."""
    play_game()

if __name__ == "__main__":
    main()
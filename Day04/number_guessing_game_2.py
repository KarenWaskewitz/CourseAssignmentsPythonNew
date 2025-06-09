import random

# Pick a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 20.")
print("Type 'x' to quit.")

while True:
    guess = input("Enter your guess: ")

    if guess.lower() == 'x':
        print("You chose to quit the game. Goodbye!")
        break

    guess = int(guess)

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct! You guessed the number!")
        break
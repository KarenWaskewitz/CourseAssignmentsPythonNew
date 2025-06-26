from game_logic import generate_number, check_guess

def play_game():
    secret = generate_number()
    guess = None
    while guess != secret:
        guess = int(input("Guess a number between 1 and 100: "))
        result = check_guess(secret, guess)
        if result == 'low':
            print("Too low!")
        elif result == 'high':
            print("Too high!")
        else:
            print("You got it!")

if __name__ == "__main__":
    play_game()
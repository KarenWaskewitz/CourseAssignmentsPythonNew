import random


def generate_number(start=1, end=100):
    """
    Returns a random number between start and end.

    >>> 1 <= generate_number(1, 10) <= 10
    True
    """
    return random.randint(start, end)


def check_guess(secret, guess):
    """
    Compares a guess to the secret number.

    >>> check_guess(50, 30)
    'low'
    >>> check_guess(50, 70)
    'high'
    >>> check_guess(50, 50)
    'correct'
    """
    if guess < secret:
        return 'low'
    elif guess > secret:
        return 'high'
    else:
        return 'correct'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
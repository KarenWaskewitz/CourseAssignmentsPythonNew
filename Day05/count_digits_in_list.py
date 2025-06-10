# count_digits_in_lists.py

def count_digits(numbers):
    digit_count = {str(d): 0 for d in range(10)}

    for number in numbers:
        for digit in str(abs(number)):
            if digit in digit_count:
                digit_count[digit] += 1

    return digit_count


if __name__ == "__main__":
    # Example list of numbers
    numbers = [1111, 5555, 8888, 33333, 22]

    result = count_digits(numbers)

    print("Digit counts:")
    for digit in sorted(result.keys()):
        print(f"{digit}: {result[digit]}")
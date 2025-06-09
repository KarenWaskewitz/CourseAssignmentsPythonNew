import re  # Regular expression module

def clean_and_sort_dna(dna_string):
    # Use regex to find all chunks made only of A, C, T, G (capital letters)
    valid_chunks = re.findall(r'[ACTG]+', dna_string)

    # Sort by length, from longest to shortest
    sorted_chunks = sorted(valid_chunks, key=len, reverse=True)

    return sorted_chunks

# Ask the user to enter a DNA sequence
dna_sequence = input("Enter your extended DNA sequence: ")

# Process the sequence
result = clean_and_sort_dna(dna_sequence)

# Display the result
print("Cleaned and sorted valid DNA chunks:")
print(result)
def clean_and_sort_dna(dna_string):
    # Split the string wherever there are 'X'
    raw_parts = dna_string.split('X')

    # Filter out empty strings and keep only valid sequences (only ACTG)
    valid_parts = [part for part in raw_parts if part and all(base in 'ACTG' for base in part)]

    # Sort by length (longest first)
    sorted_parts = sorted(valid_parts, key=len, reverse=True)

    return sorted_parts


# 🧬 Ask the user for the DNA sequence
dna_sequence = input("Enter your DNA sequence (like ACCGXXGT...): ")

# 🧪 Clean and sort
result = clean_and_sort_dna(dna_sequence)

# 📤 Show the result
print("Cleaned and sorted sequences:")
print(result)
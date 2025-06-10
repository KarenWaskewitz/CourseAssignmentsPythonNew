# count_words_from_a_file.py

import sys
import os
from collections import Counter

def count_words_in_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Normalize content: convert to lowercase and split on whitespace
    words = content.lower().split()

    # Count the words
    word_counts = Counter(words)

    # Print results
    print("\nWord counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_words_from_a_file.py <filename>")
    else:
        filename = sys.argv[1]
        count_words_in_file(filename)
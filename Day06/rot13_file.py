# rot13_file.py

import sys
import codecs
import os

def apply_rot13_to_file(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Apply ROT13 using the codecs module
    rot13_content = codecs.encode(content, 'rot_13')

    # Overwrite the file with ROT13 content
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(rot13_content)

    print(f"File '{filepath}' has been encoded with ROT13.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rot13_file.py <filename>")
    else:
        filename = sys.argv[1]
        apply_rot13_to_file(filename)

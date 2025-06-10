# count_words_in_lists.py

def count_words(word_list):
    word_count = {}

    for word in word_list:
        word = word.lower()  # optional: normalize to lowercase
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__ == "__main__":
    # Example list of words
    words = ["climate change", "because", "because", "global warming", "global warming", "temperature", "climate change"]

    result = count_words(words)

    print("Word counts:")
    for word, count in sorted(result.items()):
        print(f"{word}: {count}")
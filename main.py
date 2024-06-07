def main():
    text = get_text("books/frankenstein.txt")
    print(text)

    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    print("")

    char_count = get_char_count(text)
    letter_list = get_letter_list(char_count)
    for line in letter_list:
        print(f"The '{line['letter']}' character was found {line['count']} times")


def get_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(dict):
    return dict["count"]


def get_letter_list(char_dict):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    letter_list = []
    for char in char_dict:
        line_dict = {}
        for letter in alphabet:
            if char == letter:
                line_dict["letter"] = letter
                line_dict["count"] = char_dict[char]
                letter_list.append(line_dict)

    letter_list.sort(reverse=True, key=sort_on)
    return letter_list


main()

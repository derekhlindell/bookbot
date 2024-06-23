def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_of_words(text):
    words = len(text.split())
    return words


def get_count_of_char(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_on(dict):
    return dict["count"]


def sort_chars_by_count(char_dict):
    sorted = [] 
    for char in char_dict:
        if not char.isalpha():
            continue 
        count = char_dict.get(char)
        sorted.append({"char": char, "count": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def print_report(num_of_words, path_to_book, char_list):
    print(f"--- Here's some info about {path_to_book} ---")
    book_name = path_to_book.split("/")[1]
    print(f"There are {num_of_words} words in {book_name}!\n")
    for char_dict in char_list:
        current_char = char_dict.get("char")
        char_count = char_dict.get("count")
        print(f"The character '{current_char}' appears {char_count} times")
    print("--- End of info ---")


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_count_of_words(text)
    count_of_char = get_count_of_char(text)
    sorted_chars = sort_chars_by_count(count_of_char)
    print_report(word_count, book_path, sorted_chars)


if __name__ == "__main__":
    main()
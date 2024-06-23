def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_of_words(text):
    words = len(text.split())
    return words

def get_num_of_char(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def main():
    book_path = "books/frankenstein.txt"
    book_name = book_path.split("/")[1]
    text = get_book_text(book_path)
    num_words = get_num_of_words(text)
    print(f"{num_words} words found in {book_name}")
    char_count = get_num_of_char(text)
    print(f"Here's a dictionary with a count per character: {char_count}")

if __name__ == "__main__":
    main()
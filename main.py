def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_of_words(text):
    words = len(text.split())
    return words

def main():
    book_path = "books/frankenstein.txt"
    book_name = book_path.split("/")[1]
    text = get_book_text(book_path)
    num_words = get_num_of_words(text)
    print(f"{num_words} words found in {book_name}")

if __name__ == "__main__":
    main()
def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_content(book_path)
    book_word_count = get_book_word_count(book_text)
    print(f"This book has {book_word_count} words!")

def get_book_content(book_itself):
    with open(book_itself) as libro:
        return libro.read()

def get_book_word_count(book_text):
    data = book_text.split()
    return len(data)

main()

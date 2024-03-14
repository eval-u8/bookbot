def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_content(book_path)
    book_word_count = get_book_word_count(book_text)
    print(get_repeat_chars(book_text))

#defining fn that will read the file from its folder and return it
def get_book_content(book_itself):
    with open(book_itself) as libro:
        return libro.read()

#defining fn that will return the word count of the whole book
def get_book_word_count(book_text):
    data = book_text.split()
    return len(data)

#defining fn that will return the number of times each character appears in the book
def get_repeat_chars(book_text):
    #this way it won't show the 'enters' aka '\n' but it can also be done excluding the next two lines and passing 'book_text' instead of the 'raw_string' in the for loop
    raw_chars_array = book_text.split()
    raw_string = "".join(raw_chars_array)
    char_dict = {}
    for char in raw_string:
        lowered = char.lower()
        if char in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return(char_dict)

main()

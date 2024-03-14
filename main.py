def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_word_count = get_book_word_count(book_content)
    repeat_characters = get_repeat_chars(book_content)
    print(time_to_report(book_path, book_word_count, repeat_characters))


#defining fn that will return the word count of the whole book
def get_book_word_count(book_text):
    data = book_text.split()
    return len(data)


def time_to_report(path, word_count, char_count):
    text = f"-- Begin report of {path} -- \n {word_count} words found in the document \n\n"
    char_count_list = list(char_count.items())
    sorted_list = sorted(char_count_list, key=lambda x: x[1], reverse=True)
    for i in sorted_list:
        text += f"The '{i[0]}' character was found {i[1]} times\n"
    text= f"{text} === End Report ==="
    return text

#defining fn that will return the number of times each character appears in the book
def get_repeat_chars(book_text):
    char_dict = {}
    for char in book_text:
        lowered = char.lower()
# isalpha() method checks if characters are alphanumeric or not. returns True or False
        if not lowered.isalpha():
            pass
        elif lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return(char_dict)

#defining fn that will read the file from its folder and return it
def get_book_content(book_itself):
    with open(book_itself) as libro:
        return libro.read()

main()

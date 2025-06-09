from stats import count_words, letters, sort_dict

def get_book_text(file):
    with open(file) as f:
        book = f.read()
    return book

def report(sorted_list):
    print(
        """============ BOOKBOT ============
        Analyzing book found at books/frankenstein.txt...
        ----------- Word Count ----------
        Found 75767 total words
        --------- Character Count -------""")
    
    for dict in sorted_list:
        if dict['name'].isalpha():
            print(f"{dict['name']}: {dict['num']}")

    print("============= END ===============")

def main():
    contents = get_book_text('books/frankenstein.txt')
    total_letters = letters(contents)
    sort = sort_dict(total_letters)
    report(sort)

    

main()
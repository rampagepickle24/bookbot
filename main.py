from stats import count_words, letters, sort_dict
import sys

def get_book_text(file):
    try:
        with open(file) as f:
            book = f.read()
        return book
    except:
        print("Warning file does not exist")
        sys.exit(2)

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
    contents = get_book_text(sys.argv[1])
    total_letters = letters(contents)
    sort = sort_dict(total_letters)
    report(sort)

if len(sys.argv) != 2:
    print("Please make sure to have 2 argument: 'main.py' and 'Path to file you want read'")
    sys.exit(1)

main()
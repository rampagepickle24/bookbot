def sort_on(dict):
    return dict["num"]

def count_words(book):
    count = len(book.split())
    return count

def letters(book):
    book = book.lower()
    dict_list = []

    for letter in book:
        found = False
        for dict in dict_list:
            if dict["name"] == letter:
                dict["num"] += 1
                found = True
                break
        if not found:
            temp_dict = {"name" : letter, "num" : 1}
            dict_list.append(temp_dict)
    return dict_list

def sort_dict(dict):
    dict.sort(reverse = True, key = sort_on)
    return dict


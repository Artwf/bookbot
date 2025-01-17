# function to open book file
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = letter_count(text)
    report = dict_report(letters)
    print(f"---Begin report of {book_path} ---\n\n")
    print(f"{num_words} words in the document")
    letter_report(report)
    

# get the book text
def get_book_text(path):
    with open(path) as f:
        return f.read() 

# count the words
def get_num_words(text):
    words = text.split()
    return len(words)

# count the number of characters
def letter_count(text):
    new_dict = {}
    for letter in text:
        if letter.lower() not in new_dict:
            new_dict[letter.lower()] = 1
        else: 
            new_dict[letter.lower()] += 1
    return new_dict


# conver dictionary to report
def dict_report(book_dict):
    list_letters = []
    for i in book_dict.keys():
        if i.isalpha() == True:
            list_letters.append({i: book_dict[i]})
    my_keys = list(book_dict.keys())
    sorted_keys = []
    for i in range(len(my_keys)):
        if my_keys[i].isalpha() == True:
            sorted_keys.append(my_keys[i])
    sorted_keys.sort()
    sorted_dict = []
    for i in sorted_keys:
        sorted_dict.append({i: book_dict[i]})
    return sorted_dict

# print amount of occurences for each letter
def letter_report(file):
    for i in range(len(file)):
        for j in file[i]:
            print(f"The letter '{j}' appears {file[i][j]} times")

# call the function
main()

import sys
from stats import *

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():  
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #path_to_file ="./books/frankenstein.txt"
    path_to_file = args[1]
    print(path_to_file)

    long_string = get_book_text(path_to_file)

    num_words = get_num_words(long_string)
    print(f"Found {num_words} total words")

    sorted_character_counter = sort_character_counter(get_num_characters(long_string))

    for dict in sorted_character_counter:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")

main()
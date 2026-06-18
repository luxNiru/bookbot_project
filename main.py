from stats import book_as_string, count_characters, sort_on, chars_dict_to_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text() -> str:
    with open(sys.argv[1]) as f:
        any_text = f.read()
    return any_text

def print_report(char_dict_to_sorted_list: list[tuple[str, int]]):
    print("--------- Character Count -------")
    for char, count in char_dict_to_sorted_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    
    print("============= END ===============")

def main():
    book_path = sys.argv[1]
    book_text = get_book_text()
    total_words = book_as_string(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print_report(chars_dict_to_sorted_list(count_characters(book_text)))
    

main()
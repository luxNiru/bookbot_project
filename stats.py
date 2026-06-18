def book_as_string(get_book_text):
    book_as_word = get_book_text.split()
    num_of_words = len(book_as_word)
    return num_of_words

def count_characters(get_book_text):
    counts = {}

    lowercase_book =  get_book_text.lower()
    for i in lowercase_book:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def sort_on(counts: tuple[str, int]) -> int:
    return counts[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    counts_as_list = list(counts.items())
    sorted_counts = sorted(counts_as_list, key=sort_on, reverse=True)
    return sorted_counts
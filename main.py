import sys

from stats import get_freq_chars, get_num_words, sort_chars


def get_books_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    content = get_books_text(filepath)
    num_words = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_freq = get_freq_chars(content)
    sorted_chars = sort_chars(chars_freq)
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")


main()

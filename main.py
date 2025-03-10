import sys

from stats import get_book_text , get_letter_count, pretty_print_dict

def main() :
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    file_content = get_book_text(path_to_book)
    letter_count = get_letter_count(file_content)

    content_arr = file_content.split()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {len(content_arr)} total words")
    print("--------- Character Count -------")
    pretty_print_dict(letter_count)
    print("============= END ===============")

main()
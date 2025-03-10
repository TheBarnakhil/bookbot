def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letter_count(content) :
    alphabet_count = {}
    for char in content.lower():
        if char not in alphabet_count:
            alphabet_count[char] = 1
        else:
            alphabet_count[char] += 1
    return alphabet_count

def pretty_print_dict(letter_dict):
    letter_list = []
    char_key = "char"
    count_key = "count"
    
    def sort_on(dict):
        return dict[count_key]

    for letter in letter_dict:
        char_dict = {}
        char_dict[char_key] = letter
        char_dict[count_key] = letter_dict[letter]
        letter_list.append(char_dict)
    
    letter_list.sort(reverse=True, key=sort_on)

    for sorted_letter in letter_list:
        print(f"{sorted_letter[char_key]}: {sorted_letter[count_key]}")



    

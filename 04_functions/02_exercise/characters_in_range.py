def range_between_characters(first_char, second_char):
    range_as_ascii_symbols = []
    for num in range(ord(first_char) + 1, ord(second_char)):
        range_as_ascii_symbols.append(chr(num))
    final_string = " ".join(range_as_ascii_symbols)
    return final_string


char_one = input()
char_two = input()
print(range_between_characters(char_one, char_two))

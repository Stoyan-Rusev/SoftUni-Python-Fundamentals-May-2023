list_of_secret_words = input().split()
list_of_deciphered_words = []
for word in list_of_secret_words:
    first_letter_as_ascii_number = ''
    for ch in word:
        if ch.isnumeric():
            first_letter_as_ascii_number += ch
    print(first_letter_as_ascii_number)
    print(type(first_letter_as_ascii_number))

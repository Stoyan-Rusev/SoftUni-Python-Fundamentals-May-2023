import re
string_line = input()
pattern = r'([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
valid_pairs = re.findall(pattern, string_line)
mirror_words_list = []
result_list = []

for current_tuple in valid_pairs:
    special_symbol = current_tuple[0]
    first_word = current_tuple[1]
    second_word = current_tuple[2]

    if first_word == second_word[::-1]:
        mirror_words_list.append(current_tuple)

if valid_pairs:
    print(f"{len(valid_pairs)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words_list:
    print("The mirror words are:")
    for current_tuple in mirror_words_list:
        result_list.append(f"{current_tuple[1]} <=> {current_tuple[2]}")
    print(", ".join(result_list))
else:
    print("No mirror words!")

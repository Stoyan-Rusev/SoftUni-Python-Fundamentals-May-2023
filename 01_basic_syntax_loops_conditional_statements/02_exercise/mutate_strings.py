first_word = input()
second_word = input()
last_printed_word = first_word

for i in range(len(first_word)):
    left_part = second_word[:i + 1]
    right_part = first_word[i + 1:]
    combination = left_part + right_part
    if combination != last_printed_word:
        print(combination)
    last_printed_word = combination

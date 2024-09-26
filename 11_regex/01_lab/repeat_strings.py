string_with_words = input().split()
final_string = ''
for current_word in string_with_words:
    final_string += len(current_word) * current_word
print(final_string)

word_dict = {}
elements = input().lower().split()
for current_word in elements:
    if current_word not in word_dict.keys():
        word_dict[current_word] = 0
    word_dict[current_word] += 1

for word, occurrence in word_dict.items():
    if occurrence % 2 != 0:
        print(word, end=" ")


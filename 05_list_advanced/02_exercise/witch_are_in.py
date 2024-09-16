parts_of_words = input().split(", ")
full_words = input().split(", ")
substrings_list = []
for part in parts_of_words:
    for word in full_words:
        if part in word:
            substrings_list.append(part)
            break

print(substrings_list)

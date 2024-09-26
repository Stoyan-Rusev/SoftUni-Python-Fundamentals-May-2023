number_of_pairs_of_words = int(input())
synonym_dict = {}
for line in range(number_of_pairs_of_words):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = synonym
    else:
        synonym_dict[word] += f", {synonym}"

for key, value in synonym_dict.items():
    print(f"{key} - {value}")

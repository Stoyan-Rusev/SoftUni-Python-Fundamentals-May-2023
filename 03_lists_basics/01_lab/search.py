num_of_words = int(input())
secret_word = input()
word_list = []
final_list = []

for _ in range(num_of_words):
    word = input()
    word_list.append(word)
    if secret_word in word:
        final_list.append(word)

print(word_list)
print(final_list)

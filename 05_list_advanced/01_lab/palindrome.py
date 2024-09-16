given_words = input().split(" ")
searched_palindrome = input()
searched_palindrome_times_founded = 0
palindromes_list = []

for word in given_words:
    if word == word[::-1]:
        palindromes_list.append(word)
    if word == searched_palindrome:
        searched_palindrome_times_founded += 1

print(palindromes_list)
print(f'Found palindrome {searched_palindrome_times_founded} times')

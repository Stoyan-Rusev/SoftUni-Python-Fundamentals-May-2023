text = input()
no_vowels = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(no_vowels))

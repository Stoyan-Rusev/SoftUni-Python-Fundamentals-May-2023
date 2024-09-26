list_of_characters = input().split(", ")
ascii_dict = {ch: ord(ch) for ch in list_of_characters}
print(ascii_dict)

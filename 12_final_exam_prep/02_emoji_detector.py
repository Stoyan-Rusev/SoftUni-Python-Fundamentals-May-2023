import re


def creating_dict(all_matches: list, match_dict: dict,):
    for current_match in all_matches:
        word = current_match[1]
        word_coolness = sum([ord(ch) for ch in word])
        match_dict[word] = word_coolness
    return match_dict


text = input()
pattern = r'([:*]{2})([A-Z][a-z]{2,})\1'
threshold_pattern = r'\d'


number_matches = re.findall(threshold_pattern, text)
cool_threshold = int(number_matches[0])
for num in number_matches[1:]:
    cool_threshold *= int(num)

emoji_matches = re.findall(pattern, text)
emoji_dict = {}
emoji_dict = creating_dict(emoji_matches, emoji_dict)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_dict)} emojis found in the text. The cool ones are:")
print(emoji_matches)

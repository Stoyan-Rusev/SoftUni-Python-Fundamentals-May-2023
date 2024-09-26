text = input()
chars_counter_dict = {}
for ch in text:
    if ch != " ":
        if ch not in chars_counter_dict:
            chars_counter_dict[ch] = 0
        chars_counter_dict[ch] += 1

for key, value in chars_counter_dict.items():
    print(f"{key} -> {value}")

import re
text = input()
pattern = r"\b(_)([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, text)
# print(matches)
final_list = []
for current_tuple in matches:
    final_list.append(current_tuple[1])

print(",".join(final_list))

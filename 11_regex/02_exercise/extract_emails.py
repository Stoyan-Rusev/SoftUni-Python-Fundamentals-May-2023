import re

text_line = input()
pattern = r"\s(([a-z0-9]+[\.\,\-\_a-z0-9]*)@([a-z][a-z\-]+)(\.[a-z\-]+)+)\b"
matches = re.findall(pattern, text_line)
for current_match in matches:
    print(current_match[0])

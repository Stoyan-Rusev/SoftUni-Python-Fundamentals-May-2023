import re
line = input()

while line:
    pattern = r"\d+"
    matches = re.findall(pattern, line)
    for match in matches:
        print(match, end=" ")
    line = input()

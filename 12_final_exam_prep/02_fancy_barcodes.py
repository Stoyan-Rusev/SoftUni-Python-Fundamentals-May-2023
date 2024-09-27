import re

lines = int(input())
pattern = r'(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])\1'
matches = []

for line in range(lines):
    text = input()
    match = re.search(pattern, text)

    if match:
        matches.append(match.group(2))
    else:
        matches.append("Invalid barcode")
# print(matches)

for current_match in matches:
    if current_match == "Invalid barcode":
        print("Invalid barcode")
    else:
        group_name = ''

        for ch in current_match:
            if ch.isnumeric():
                group_name += ch
        if group_name == '':
            print(f"Product group: {'00'}")
        else:
            print(f"Product group: {group_name}")

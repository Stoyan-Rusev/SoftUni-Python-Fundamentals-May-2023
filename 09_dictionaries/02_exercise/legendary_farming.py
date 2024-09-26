items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained_item = ''
mission_completed = False

while not mission_completed:
    found_items = []
    found_quantity = []
    line_with_strings = input().split()
    for index in range(0, len(line_with_strings), 2):
        found_items.append(line_with_strings[index + 1].lower())
        found_quantity.append(int(line_with_strings[index]))
    for i in range(len(found_items)):
        if found_items[i] not in items.keys():
            items[found_items[i]] = found_quantity[i]
        else:
            items[found_items[i]] += found_quantity[i]

        if items['shards'] >= 250:
            mission_completed = True
            obtained_item = 'Shadowmourne'
            items['shards'] -= 250
            break
        elif items['fragments'] >= 250:
            mission_completed = True
            obtained_item = 'Valanyr'
            items['fragments'] -= 250
            break
        elif items['motes'] >= 250:
            mission_completed = True
            obtained_item = 'Dragonwrath'
            items['motes'] -= 250
            break
print(f"{obtained_item} obtained!")
for key, value in items.items():
    print(f"{key}: {value}")

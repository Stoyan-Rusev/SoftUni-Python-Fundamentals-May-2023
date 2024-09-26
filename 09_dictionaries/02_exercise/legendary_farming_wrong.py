key_materials = {"shards": 0,
                 "fragments": 0,
                 "motes": 0
                 }
junk_materials = {}
item_obtained = ''
mission_completed = False
while not mission_completed:
    keys = []
    values = []
    text = input().split()
    for index in range(0, len(text), 2):
        values.append(int(text[index]))
        keys.append(text[index + 1].lower())

    found_materials_values = {keys[i]: values[i] for i in range(len(keys))}
    for current_material, current_value in found_materials_values.items():
        if mission_completed:
            break
        if current_material in key_materials.keys():
            key_materials[current_material] += current_value
        elif current_material in junk_materials.keys():
            junk_materials[current_material] += current_value
        else:
            junk_materials[current_material] = current_value
        for material in key_materials.keys():
            if key_materials[material] >= 250:
                mission_completed = True
                key_materials[material] -= 250
                if material == "shards":
                    item_obtained = "Shadowmourne"
                elif material == "fragments":
                    item_obtained = "Valanyr"
                elif material == "motes":
                    item_obtained = "Dragonwrath"
                break

print(f"{item_obtained} obtained!")
for mat, val in key_materials.items():
    print(f"{mat}: {val}")
for mat, val in junk_materials.items():
    print(f"{mat}: {val}")

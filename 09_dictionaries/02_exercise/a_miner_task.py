stash_dict = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in stash_dict.keys():
        stash_dict[resource] = quantity
    else:
        stash_dict[resource] += quantity

for key, value in stash_dict.items():
    print(f"{key} -> {value}")

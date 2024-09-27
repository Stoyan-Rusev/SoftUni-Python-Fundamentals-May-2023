def contains(activation_key, substring):
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    return "Substring not found!"


def flipping(activation_key, type_flipping, index_one, index_two):
    if type_flipping == 'Upper':
        flip_string = activation_key[index_one:index_two].upper()
        new_key = activation_key[0:index_one] + flip_string + activation_key[index_two:]
        return new_key
    elif type_flipping == 'Lower':
        flip_string = activation_key[index_one:index_two].lower()
        new_key = activation_key[0:index_one] + flip_string + activation_key[index_two:]
        return new_key


def slicing(activation_key, index_one, index_two):
    new_key = activation_key[0:index_one] + activation_key[index_two:]
    return new_key


raw_activation_key = input()
command = input()
while command != 'Generate':
    command = command.split(">>>")
    action = command[0]
    if action == 'Contains':
        key_substring = command[1]
        print(contains(raw_activation_key, key_substring))
    elif action == 'Flip':
        flipping_type = command[1]
        starting_index = int(command[2])
        ending_index = int(command[3])
        raw_activation_key = flipping(raw_activation_key, flipping_type, starting_index, ending_index)
        print(raw_activation_key)
    elif action == 'Slice':
        starting_index = int(command[1])
        ending_index = int(command[2])
        raw_activation_key = slicing(raw_activation_key, starting_index, ending_index)
        print(raw_activation_key)

    command = input()
print(f'Your activation key is: {raw_activation_key}')

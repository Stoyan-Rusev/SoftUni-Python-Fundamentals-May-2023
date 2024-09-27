def adding_stop(string: str, values: list):
    index = int(values[0])
    added_string = values[1]
    if index in range(len(string)):
        first_half = string[:index]
        second_half = string[index:]
        string = first_half + added_string + second_half
    return string


def removing_stop(string: str, values: list):
    start_index = int(values[0])
    end_index = int(values[1])
    if start_index in range(len(string)) and end_index in range(len(string)):
        string = string[:start_index] + string[end_index + 1:]
    return string


def switching(string: str, values: list):
    old_string = values[0]
    new_string = values[1]
    if old_string in string:
        string = string.replace(old_string, new_string)
    return string


initial_string = input()
command = input()
while command != 'Travel':
    action, *params = command.split(':')
    if action == 'Add Stop':
        initial_string = adding_stop(initial_string, params)
        print(initial_string)
    elif action == 'Remove Stop':
        initial_string = removing_stop(initial_string, params)
        print(initial_string)
    elif action == 'Switch':
        initial_string = switching(initial_string, params)
        print(initial_string)
    command = input()
print(f"Ready for world tour! Planned stops: {initial_string}")

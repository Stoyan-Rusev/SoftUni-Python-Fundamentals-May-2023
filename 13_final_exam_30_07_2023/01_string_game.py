def changing(some_string: str, parameters: list):
    char = parameters[0]
    replacement = parameters[1]
    some_string = some_string.replace(char, replacement)
    print(some_string)
    return some_string


def including(some_string: str, parameters: list):
    substring = parameters[0]
    if substring in some_string:
        print("True")
    else:
        print("False")
    return some_string


def uppercase(some_string: str):
    some_string = some_string.upper()
    return some_string


def ending_with(some_string: str, parameters: list):
    substring = parameters[0]
    if some_string.endswith(substring):
        print("True")
    else:
        print("False")
    return some_string


def finding_index(some_string: str, parameters: list):
    char = parameters[0]
    for i, ch in enumerate(some_string):
        if ch == char:
            print(i)
    return some_string


def cutting(some_string: str, parameters: list):
    starting_index = int(parameters[0])
    count = int(parameters[1])
    cutted_string = some_string[starting_index:starting_index + count]
    print(cutted_string)
    return cutted_string


string = input()
command = input()
while command != 'Done':
    action, *params = command.split()
    if action == 'Change':
        string = changing(string, params)
    elif action == 'Includes':
        string = including(string, params)
    elif action == 'End':
        string = ending_with(string, params)
    elif action == 'Uppercase':
        print(uppercase(string))
    elif action == 'FindIndex':
        string = finding_index(string, params)
    elif action == 'Cut':
        string = cutting(string, params)
    command = input()

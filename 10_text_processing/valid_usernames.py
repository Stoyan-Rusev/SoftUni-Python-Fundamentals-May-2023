def length_is_valid(username):
    if 3 <= len(username) <= 6:
        return True
    return False


def valid_symbols(username: str):
    for symbol in username:
        if symbol.isalnum() or symbol == '-' or symbol == '_':
            return True
        return False


def is_valid(username):
    if valid_symbols(username) and length_is_valid(username):
        return True
    return False


names_list = input().split(", ")
for name in names_list:
    if is_valid(name):
        print(name)

import re


def validating_password(some_password: str):
    pattern = r'(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1'
    match = re.search(pattern, some_password)
    if not match:
        message = 'Try another password!'
    else:
        encrypted_password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
        message = f"Password: {encrypted_password}"
    return message


num_of_inputs = int(input())
for current_line in range(num_of_inputs):
    current_password = input()
    print(validating_password(current_password))

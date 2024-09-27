def moving(message: str, values: list):
    first_letters_num = int(values[0])
    first_part = message[:first_letters_num]
    second_part = message[first_letters_num:]
    swapped_message = second_part + first_part
    return swapped_message


def inserting(message: str, values: list):
    index = int(values[0])
    value = values[1]
    first_part = message[:index]
    second_part = message[index:]
    new_message = first_part + value + second_part
    return new_message


def changing_all(message: str, values: list):
    substring = values[0]
    replacement_text = values[1]
    if substring in message:
        message = message.replace(substring, replacement_text)
    return message


encrypted_message = input()
command = input()
while command != 'Decode':
    action, *params = command.split('|')
    if action == 'Move':
        encrypted_message = moving(encrypted_message, params)
    elif action == 'Insert':
        encrypted_message = inserting(encrypted_message, params)
    elif action == 'ChangeAll':
        encrypted_message = changing_all(encrypted_message, params)
    command = input()
print(f"The decrypted message is: {encrypted_message}")

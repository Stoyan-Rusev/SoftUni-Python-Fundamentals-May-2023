def inserting_space(secret_message, data_list: list):
    index = int(data_list[1])
    secret_message = secret_message[:index] + " " + secret_message[index:]
    return secret_message


def reversing(secret_message: str, data_list: list):
    substring = data_list[1]
    if substring not in secret_message:
        print("error")
    elif substring in secret_message:
        secret_message = secret_message.replace(substring, "", 1)
        secret_message += substring[::-1]
        print(secret_message)
    return secret_message


def changing_all(secret_message: str, data_list: list):
    substring = data_list[1]
    replacing_string = data_list[2]
    if substring in secret_message:
        secret_message = secret_message.replace(substring, replacing_string)
    return secret_message


message = input()
command = input()
while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        message = inserting_space(message, command)
        print(message)
    elif action == "Reverse":
        message = reversing(message, command)
    elif action == "ChangeAll":
        message = changing_all(message, command)
        print(message)
    command = input()
print(f"You have a new text message: {message}")

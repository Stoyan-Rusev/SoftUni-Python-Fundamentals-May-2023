number_of_messages = int(input())
number = 0
message = ''

for i in range(number_of_messages):
    number = int(input())
    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88 and number != 86:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
    
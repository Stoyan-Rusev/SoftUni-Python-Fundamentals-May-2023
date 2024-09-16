def calculator(operator, num_one, num_two):
    if operator == "multiply":
        return num_one * num_two
    elif operator == "divide":
        return int(num_one / num_two)
    elif operator == "add":
        return num_one + num_two
    elif operator == "subtract":
        return num_one - num_two


input_operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(input_operator, first_number, second_number))

def factorial(number):
    factorial_sum = number
    for current_num in range(1, number):
        factorial_sum *= current_num
    return factorial_sum


first_number = int(input())
second_number = int(input())
result = factorial(first_number) / factorial(second_number)
print(f"{result:.2f}")

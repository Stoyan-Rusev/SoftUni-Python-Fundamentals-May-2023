def is_even(number):
    if number % 2 == 0:
        return number


numbers = input().split()
list_of_int_numbers = []
for num in numbers:
    list_of_int_numbers.append(int(num))

result = list(filter(is_even, list_of_int_numbers))
print(result)

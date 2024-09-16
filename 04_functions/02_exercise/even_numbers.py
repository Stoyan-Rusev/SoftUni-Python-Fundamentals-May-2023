def is_even(number):
    list_of_even_numbers = []
    for num in number:
        if int(num) % 2 == 0:
            list_of_even_numbers.append(int(num))
    return list_of_even_numbers


numbers = input().split()
print(is_even(numbers))

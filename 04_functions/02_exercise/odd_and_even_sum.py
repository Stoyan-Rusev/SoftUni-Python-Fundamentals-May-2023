def odd_even_sum(number_as_string):
    sum_of_even = 0
    sum_of_odd = 0

    for symbol in number_as_string:
        if int(symbol) % 2 == 0:
            sum_of_even += int(symbol)
        else:
            sum_of_odd += int(symbol)

    return sum_of_even, sum_of_odd


number = input()
sum_of_even_numbers, sum_of_odd_numbers = odd_even_sum(number)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")

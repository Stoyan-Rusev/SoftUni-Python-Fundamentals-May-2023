numbers = input().split()
numbers_as_digits = []
sorted_numbers = []

for num in numbers:
    numbers_as_digits.append(int(num))

sorted_numbers = sorted(numbers_as_digits)
print(sorted_numbers)

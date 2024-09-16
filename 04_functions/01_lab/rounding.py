items_as_strings = input().split()
rounded_digits_list = []
for digit in items_as_strings:
    rounded_digits_list.append(round(float(digit)))

print(rounded_digits_list)

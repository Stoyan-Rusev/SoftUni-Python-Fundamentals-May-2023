numbers = input().split(", ")

positive_numbers = [number for number in numbers if int(number) >= 0]
negative_numbers = [number for number in numbers if int(number) < 0]
even_numbers = [number for number in numbers if int(number) % 2 == 0]
odd_numbers = [number for number in numbers if int(number) % 2 != 0]

positive = ", ".join(positive_numbers)
negative = ", ".join(negative_numbers)
even = ", ".join(even_numbers)
odd = ", ".join(odd_numbers)

print(f"Positive: {positive}\n"
      f"Negative: {negative}\n"
      f"Even: {even}\n"
      f"Odd: {odd}")

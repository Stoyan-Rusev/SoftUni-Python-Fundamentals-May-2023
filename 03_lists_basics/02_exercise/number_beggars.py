money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_digits = []
for money in money_as_string:
    money_as_digits.append(int(money))

staring_index = 0
final_scores = []

while staring_index < number_of_beggars:
    current_beggar_money = 0
    for current_index in range(staring_index, len(money_as_string), number_of_beggars):
        current_beggar_money += money_as_digits[current_index]
    final_scores.append(current_beggar_money)
    staring_index += 1

print(final_scores)

n = int(input())
list_positive = []
list_negative = []

for _ in range(n):
    number = int(input())
    if number < 0:
        list_negative.append(number)
    else:
        list_positive.append(number)

count_of_positives = len(list_positive)
sum_of_negatives = 0

for number in list_negative:
    sum_of_negatives += number
print(list_positive)
print(list_negative)
print(f"Count of positives: {count_of_positives}\nSum of negatives: {sum_of_negatives}")

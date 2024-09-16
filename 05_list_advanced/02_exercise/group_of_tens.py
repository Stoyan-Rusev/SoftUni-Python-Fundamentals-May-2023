from math import ceil


def amount_of_groups(list_of_numbers):
    biggest_num = (max(list_of_numbers))
    groups = ceil(biggest_num/10)
    return groups


number_lst = [int(number) for number in input().split(", ")]

for current_group in range(1, amount_of_groups(number_lst) + 1):
    current_num_list = []
    for num in number_lst:
        if (current_group - 1) * 10 < num <= current_group * 10:
            current_num_list.append(num)
    print(f"Group of {current_group}0's: {current_num_list}")

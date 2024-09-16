number_lst = [int(number) for number in input().split(", ")]
current_num_group = 10

while number_lst:
    current_list = []

    for num in number_lst:
        if num <= current_num_group:
            current_list.append(num)

    print(f"Group of {current_num_group}'s: {current_list}")
    current_num_group += 10
    number_lst = [number for number in number_lst if number not in current_list]

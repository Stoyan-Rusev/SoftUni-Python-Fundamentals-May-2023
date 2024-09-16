def find_even_index(list_of_integers: list):
    even_indexes = []
    for current_num in list_of_integers:
        if current_num % 2 == 0:
            even_indexes.append(list_of_integers.index(current_num))
    return even_indexes


number_List = list(map(int, input().split(", ")))
print(find_even_index(number_List))

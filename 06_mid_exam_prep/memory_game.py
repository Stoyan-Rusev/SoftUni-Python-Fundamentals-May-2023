def sequence_twins(sequence_with_items, first_index, second_index, number_of_moves):
    if first_index not in range(len(sequence_with_items)) or \
            second_index not in range(len(sequence_with_items)) or \
            first_index == second_index:
        sequence_with_items.insert(len(sequence_with_items) // 2, f"-{number_of_moves}a")
        sequence_with_items.insert(len(sequence_with_items) // 2, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_with_items[first_index] == sequence_with_items[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_with_items[first_index]}!")
            removed_item = sequence_with_items.pop(first_index)
            sequence_with_items.remove(removed_item)
        else:
            print("Try again!")
    return sequence_with_items


sequence = input().split(" ")
command = input()
moves = 0
while command != "end":
    moves += 1
    command = command.split(" ")
    index_one = int(command[0])
    index_two = int(command[1])
    sequence = sequence_twins(sequence, index_one, index_two, moves)
    if not sequence:
        print(f"You have won in {moves} turns!")
        break
    command = input()
if sequence:
    print("Sorry you lose :(")
    print(*sequence)

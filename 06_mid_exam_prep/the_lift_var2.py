WAGON_CAPACITY = 4
waiting_people = int(input())
lift = [int(wagon) for wagon in input().split(' ')]

for index, current_wagon in enumerate(lift):
    if current_wagon < WAGON_CAPACITY:  # --> wagon has free spaces
        free_seats = WAGON_CAPACITY - current_wagon
        if waiting_people >= free_seats:  # --> filling the wagon IF there are enough people for it
            waiting_people -= free_seats
            lift[index] = WAGON_CAPACITY
            if index == len(lift) - 1:   # --> check if this is the last wagon
                if waiting_people == 0:  # --> lift full, no people in queue
                    print(*lift)
                    break
                else:                    # --> lift full, people in queue
                    print(f"There isn't enough space! {waiting_people} people in a queue!")
                    print(*lift)
                    break

        elif waiting_people < free_seats:  # --> there is space but no more people
            lift[index] += waiting_people
            print("The lift has empty spots!")
            print(*lift)
            break

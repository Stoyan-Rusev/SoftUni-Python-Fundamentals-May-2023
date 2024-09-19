def filling_the_wagons(wagons, people_on_queue):
    for index, current_wagon in enumerate(wagons):
        if current_wagon < MAX_CAPACITY:
            free_spaces = MAX_CAPACITY - current_wagon
            if people_on_queue >= free_spaces:
                wagons[index] += free_spaces
                people_on_queue -= free_spaces
            elif people_on_queue < free_spaces:
                wagons[index] += people_on_queue
                people_on_queue = 0
            # print(wagons)
            # print(people_on_queue)
    return state_of_wagons, people_on_queue


MAX_CAPACITY = 4
waiting_people = int(input())
state_of_wagons = [int(wagon) for wagon in input().split(" ")]

state_of_wagons, waiting_people = (state_of_wagons, waiting_people)
if waiting_people == 0 and sum(state_of_wagons) / len(state_of_wagons) < 4:
    print(f"The lift has empty spots!")
    print(*state_of_wagons)






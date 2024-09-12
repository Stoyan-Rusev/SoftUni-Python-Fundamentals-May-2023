number_of_people = int(input())
elevator_capacity = int(input())

courses = number_of_people // elevator_capacity
people_left_for_final_course = number_of_people % elevator_capacity

if elevator_capacity >= number_of_people:
    print('All the persons fit inside the elevator.\nOnly one course is needed.')
else:
    if number_of_people % elevator_capacity == 0:
        print(f"{courses} courses * {elevator_capacity} people")
    else:
        print(f"{courses} courses * {elevator_capacity} people")
        print(f"+ 1 course * {people_left_for_final_course} persons")

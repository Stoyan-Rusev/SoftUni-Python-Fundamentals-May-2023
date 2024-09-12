from math import ceil
number_of_people = int(input())
elevator_capacity = int(input())

total_courses = ceil(number_of_people / elevator_capacity)
print(total_courses)

from math import ceil

number_of_students = int(input())
num_of_lectures = int(input())
additional_bonus = int(input())
winner_bonus = 0
winner_attendances = 0

for current_student in range(1, number_of_students + 1):
    student_attendances = int(input())
    total_bonus = student_attendances / num_of_lectures * (5 + additional_bonus)
    if total_bonus > winner_bonus:
        winner_bonus = total_bonus
        winner_attendances = student_attendances

print(f"Max Bonus: {ceil(winner_bonus)}.")
print(f"The student has attended {winner_attendances} lectures.")

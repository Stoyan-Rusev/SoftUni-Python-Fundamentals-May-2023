num_of_iterations = int(input())
students_grades_dict = {}

for line in range(num_of_iterations):
    name = input()
    grade = float(input())
    if name not in students_grades_dict.keys():
        students_grades_dict[name] = []
    students_grades_dict[name].append(grade)

for current_student in students_grades_dict.keys():
    if (sum(students_grades_dict[current_student]) / len(students_grades_dict[current_student])) < 4.50:
        pass

for current_student, current_grade in students_grades_dict.items():
    print(f"{current_student} -> {sum(students_grades_dict[current_student]) / len(students_grades_dict[current_student]):.2f}")

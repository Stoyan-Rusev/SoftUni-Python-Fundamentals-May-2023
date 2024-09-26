students_info = input().split(":")
courses_dict = {}
while len(students_info) == 3:
    student_name, student_id, course = students_info
    courses_dict[student_name] = [student_id, course]
    students_info = input().split(":")

searched_course = students_info[0]
for current_student, list_with_info in courses_dict.items():
    if list_with_info[1].startswith(searched_course[0:3]):
        print(f"{current_student} - {list_with_info[0]}")

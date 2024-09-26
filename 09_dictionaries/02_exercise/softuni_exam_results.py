names_points = {}
courses_submissions = {}

student_data = input().split("-")
while student_data[0] != 'exam finished':
    if len(student_data) == 3:
        name, course, points = student_data[0], student_data[1], int(student_data[2])
        if name not in names_points.keys():
            names_points[name] = points
        else:
            if points > names_points[name]:
                names_points[name] = points

        if course not in courses_submissions:
            courses_submissions[course] = 0
        courses_submissions[course] += 1
    else:   # student is banned
        name = student_data[0]
        if name in names_points.keys():
            del names_points[name]

    student_data = input().split("-")

print('Results:')
for name, points in names_points.items():
    print(f"{name} | {points}")
print('Submissions:')
for course, submissions in courses_submissions.items():
    print(f'{course} - {submissions}')

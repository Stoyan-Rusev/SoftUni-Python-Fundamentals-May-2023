courses = {}
command = input().split(" : ")
while command[0] != 'end':
    course, student = command[0], command[1]
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)
    command = input().split(" : ")
for current_course in courses.keys():
    print(f"{current_course }: {len(courses[current_course])}")
    for current_student in courses[current_course]:
        print(f"-- {current_student}")

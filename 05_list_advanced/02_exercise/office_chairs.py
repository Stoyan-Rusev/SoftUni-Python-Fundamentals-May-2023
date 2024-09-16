rooms = int(input())
free_chairs = 0
is_there_free_chairs = True
for room in range(1, rooms + 1):
    chairs, people = input().split(" ")
    people = int(people)
    if len(chairs) < people:
        is_there_free_chairs = False
        print(f"{people - len(chairs)} more chairs needed in room {room}")

    else:
        free_chairs += (len(chairs) - people)

if is_there_free_chairs:
    print(f"Game On, {free_chairs} free chairs left")

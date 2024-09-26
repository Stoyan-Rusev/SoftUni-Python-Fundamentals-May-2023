phonebook = {}
num_of_searching = 0
while True:
    people_and_number = input()
    if "-" not in people_and_number:
        num_of_searching = int(people_and_number)
        break
    current_people, current_number = people_and_number.split("-")
    phonebook[current_people] = current_number

for time_searching in range(num_of_searching):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

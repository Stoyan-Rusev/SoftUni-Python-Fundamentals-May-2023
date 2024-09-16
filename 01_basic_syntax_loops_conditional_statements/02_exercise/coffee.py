one_coffee_commands = ["coding", "dog", "cat", "movie"]
two_coffee_commands = [word.upper() for word in one_coffee_commands]

current_word = input()
coffee_counter = 0
while current_word != 'END':
    if current_word in one_coffee_commands:
        coffee_counter += 1
    elif current_word in two_coffee_commands:
        coffee_counter += 2
    current_word = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

number_of_letters = int(input())
for a in range(number_of_letters):
    first_letter = ord("a") + a
    for b in range(number_of_letters):
        second_letter = ord("a") + b
        for c in range(number_of_letters):
            third_letter = ord("a") + c
            print(chr(first_letter) + chr(second_letter) + chr(third_letter))

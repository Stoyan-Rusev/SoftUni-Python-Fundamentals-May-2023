number = int(input())
for current_num in range(1, number + 1):
    if current_num < 10:
        if current_num == 5 or current_num == 7:
            print(f"{current_num} -> True")
        else:
            print(f"{current_num} -> False")

    elif current_num >= 10:
        current_num = str(current_num)
        if int(current_num[0]) + int(current_num[1]) == 5:
            print(f"{current_num} -> True")
        elif int(current_num[0]) + int(current_num[1]) == 7:
            print(f"{current_num} -> True")
        elif int(current_num[0]) + int(current_num[1]) == 11:
            print(f"{current_num} -> True")

        else:
            print(f"{current_num} -> False")

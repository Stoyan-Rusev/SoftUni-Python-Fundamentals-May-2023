def validator(password):
    result = "Password is valid"
    digit_counter = 0

    if 6 <= len(password) <= 10:
        for element in password:
            if 48 <= ord(element) <= 57:     # numbers
                digit_counter += 1
            elif 65 <= ord(element) <= 90:   # upper chars
                continue
            elif 97 <= ord(element) <= 122:  # lower chars
                continue
            else:
                result = "Password must consist only of letters and digits"
                break

        if digit_counter < 2:
            result = "Password must have at least 2 digits"

    else:
        result = "Password must be between 6 and 10 characters"

    return result


current_password = input()
print(validator(current_password))

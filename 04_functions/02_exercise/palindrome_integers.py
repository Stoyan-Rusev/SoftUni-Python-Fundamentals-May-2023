def palindrome(list_positive_integers):
    for num in list_positive_integers:
        is_palindrome = False
        if num[::-1] == num:
            is_palindrome = True
        print(is_palindrome)


numbers = input().split(", ")
palindrome(numbers)

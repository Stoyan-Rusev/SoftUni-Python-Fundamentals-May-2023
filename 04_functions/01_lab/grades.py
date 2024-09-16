def convert_grade_to_word(grade):
    if 2.00 <= grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif grade <= 6.00:
        return "Excellent"


current_grade = float(input())
print(convert_grade_to_word(current_grade))

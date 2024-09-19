first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())
total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hour_counter = 0


while number_of_students > 0:
    hour_counter += 1
    if hour_counter % 4 == 0:
        hour_counter += 1
    number_of_students -= total_efficiency

print(f"Time needed: {hour_counter}h.")

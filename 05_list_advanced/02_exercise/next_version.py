version = input().split(".")
version_as_number = int("".join(version))
next_version_as_number = version_as_number + 1
first_num = str(next_version_as_number)[0]
second_num = str(next_version_as_number)[1]
third_num = str(next_version_as_number)[2]
next_version = f"{first_num}.{second_num}.{third_num}"
print(next_version)


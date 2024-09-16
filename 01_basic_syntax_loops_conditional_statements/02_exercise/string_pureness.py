num_inputs = int(input())
for n in range(num_inputs):
    some_string = input()
    if "_" in some_string or "." in some_string or "," in some_string:
        print(f"{some_string} is not pure!")
    else:
        print(f"{some_string} is pure.")

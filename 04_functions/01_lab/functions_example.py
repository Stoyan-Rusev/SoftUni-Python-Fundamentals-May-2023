def sum_numbers(a: int, b: int) -> int:
    return a + b


def string_sum(a: str, b: str):
    print(a + b)


for _ in range(2):
    c = input()
    f = input()
    print(string_sum(c, f))

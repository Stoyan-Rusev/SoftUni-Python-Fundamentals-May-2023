year = int(input())
while True:
    year += 1
    year_str = str(year)
    if len(set(year_str)) == len(str(year)):
        print(year)
        break

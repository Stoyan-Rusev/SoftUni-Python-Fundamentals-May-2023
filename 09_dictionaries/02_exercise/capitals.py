countries = input().split(", ")
capitals = input().split(", ")
country_capital_dict = {countries[index]: capitals[index] for index in range(len(countries))}
for current_country, current_capital in country_capital_dict.items():
    print(f"{current_country} -> {current_capital}")

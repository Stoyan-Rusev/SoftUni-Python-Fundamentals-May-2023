import re

text = input()
pattern = r"([/=])([A-Z]{1}[A-Za-z]{2,})\1"
matches = re.finditer(pattern, text)
travel_points = 0
destinations = []

for current_match in matches:
    city = current_match.group(2)
    destinations.append(city)
    travel_points += len(city)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")

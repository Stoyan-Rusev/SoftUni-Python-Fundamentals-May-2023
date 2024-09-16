def rectangle_area(width, height):
    area = width * height
    return area


current_width = int(input())
current_height = int(input())
result = rectangle_area(current_width, current_height)
print(result)
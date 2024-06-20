import math

def circle_states(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle_states(5)

print("Area of circle:", "{:.2f}".format(area), "\nCircumference of circle:", "{:.2f}".format(circumference))
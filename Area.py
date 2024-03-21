# Square
side_length = 5
square_area = side_length ** 2
square_perimeter = 4 * side_length

# Rectangle
rectangle_length = 6
rectangle_width = 4
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)

# Triangle
triangle_base = 8
triangle_height = 5
triangle_side1 = 7
triangle_side2 = 7
triangle_side3 = 7
triangle_s = (triangle_side1 + triangle_side2 + triangle_side3) / 2
triangle_area = (triangle_s * (triangle_s - triangle_side1) * (triangle_s - triangle_side2) * (triangle_s - triangle_side3)) ** 0.5
triangle_perimeter = triangle_side1 + triangle_side2 + triangle_side3

# Circle
circle_radius = 3
circle_area = 3.14159 * circle_radius ** 2
circle_perimeter = 2 * 3.14159 * circle_radius


print("Square: Area =" , square_area , "Perimeter =" , square_perimeter)
print("Rectangle: Area = ",rectangle_area, "Perimeter =", rectangle_perimeter)
print("Triangle: Area = " ,triangle_area," Perimeter =", triangle_perimeter)
print("Circle: Area = " ,circle_area, "Perimeter =", circle_perimeter)

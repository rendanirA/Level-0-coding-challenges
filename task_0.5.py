def area_of_a_triangle(side1, side2, side3):
    semi_parimeter = 1 / 2 * (side1 + side2 + side3)
    semi_perimeter_minus_side1 = semi_parimeter - side1
    semi_perimeter_minus_side2 = semi_parimeter - side2
    semi_perimeter_minus_side3 = semi_parimeter - side3
    area = (
        semi_parimeter
        * (semi_perimeter_minus_side1)
        * (semi_perimeter_minus_side2)
        * (semi_perimeter_minus_side3)
    )
    return sqrt(area)**0.5


print(area_of_a_triangle(3, 4, 5))





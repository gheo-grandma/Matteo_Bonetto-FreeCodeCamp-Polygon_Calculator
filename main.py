# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(3)
print(sq.get_area())
print(sq.get_perimeter())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

print(rect.get_picture())
print(sq.get_picture())

print(rect.get_amount_inside(sq))

sq2 = shape_calculator.Square(12)
sq.set_side(3)

print(sq.get_picture())
print("\n")
print(sq2.get_picture())
print(sq2.get_amount_inside(sq))


# Run unit tests automatically
#main(module='test_module', exit=False)

print("ready")

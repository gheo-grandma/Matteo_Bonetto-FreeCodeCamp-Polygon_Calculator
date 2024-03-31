class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Setters
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  # Getters
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    # Sum of all edges
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    # Pythogoras theorem
    return ((self.width**2) + (self.height**2))**.5

  def get_picture(self):
    # Error handling
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    else:
      return (("*" * self.width) + "\n") * self.height

  def get_amount_inside(self, shape):
    # Check if a polygon's side is not bigger than the other
    if self.width > shape.width or self.height > shape.width:
      if self.height > shape.height or self.height > shape.width:
        
        return False
    # Use the area to check how many of shape I can fit inside
    return int(shape.get_area() / self.get_area())

  # Readable format output
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  # Override inherited methods from Rectangle
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_heigth(self, height):
    self.width = height
    self.height = height

  def __str__(self):
    return f"Square(side={self.width})"

class Circle(object):

  def __init__(self, radius = 10):
    self.radius = radius
    self.pi = 3.1459

  def perimeter(self):
    return (2 * self.pi * self.radius)

  def area(self):
    return (pow(self.pi, 2) * self.radius)
    
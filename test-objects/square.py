class Square(object):

  def __init__(self, side = 5):
    self.side = side

  def area(self):
    return (pow(self.side, 2))

  def perimeter(self):
    return (4 * self.side)

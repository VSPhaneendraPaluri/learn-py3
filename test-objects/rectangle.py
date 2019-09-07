class Rectangle(object):

  def __init__ (self, a = 5, b = 10):
    self.length = a
    self.breadth = b

  def area(self):
    return (self.length * self.breadth)

  def perimeter(self):
    return (2*(self.length + self.breadth))

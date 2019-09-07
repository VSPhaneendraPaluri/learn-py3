'''
This tutorial demonstrates the use of test markers in enabling
test parameterization for PYTEST

Run the parametrized tests by running
  >$ pytest <filename.py> -v

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

@pytest.mark.parametrize('length, breadth, area, perimeter',
  [
    ( 1,  2,   2,  6),
    (13, 12, 156, 50),
    (10, 20, 200, 60)
  ])
def test_AreaOfARectangleWithTestVectors(length, breadth, area, perimeter):
  rectangle = Rectangle(length, breadth)
  assert rectangle.area() == area
  assert rectangle.perimeter() == perimeter


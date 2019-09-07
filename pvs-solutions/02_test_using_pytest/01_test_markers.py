'''
This tutorial demonstrates the use of test markers made available for PYTEST

The users could easily appreciate the use of markers that enable users to filter tests
based upon the markers

Exercise the following :
1. Use the switch -m <Marker> to select / filter the intended tests marked with the <Marker>
   Eg. >$ pytest <filename.py> -m <Marker> -v

2. Use the switch -k to select / filter the tests containing the provided names
   Eg. >$ pytest <filename.py> -k <NameSelection> -v

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

@pytest.mark.default
def test_AreaOfARectangleWithDefaultSide():
  rectangle = Rectangle()
  assert rectangle.area() == 50, "Value should be 50"

@pytest.mark.user
def test_AreaOfARectangleWithNonDefaultSide():
  rectangle = Rectangle(10, 20)
  assert rectangle.area() == 200, "Value should be 200"

@pytest.mark.user
def test_PerimeterOfRectangleWithNonDefaultSide():
  rectangle = Rectangle(12, 13)
  assert rectangle.perimeter() == 50, "Perimeter is 2*length + 2*breadth = 50"

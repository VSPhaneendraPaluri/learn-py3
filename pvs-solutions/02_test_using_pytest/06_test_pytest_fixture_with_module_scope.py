'''
This tutorial demonstrates the use of PYTEST fixture highlighting
module scope

NOTE : Try running the tutorial example in verbose mode with arguments --capture=no

NOTE : This tutorial highlights and answers to
1. What does one observe from the run log ?
2. What does one need to do in order to have setup
   called only once per module scope

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

@pytest.fixture(scope="module")
def getDefaultRectangleObject():
  print("\nSetUp called ...")
  rectangles = Rectangle()
  yield rectangles
  print("\nTearDown called ...")

def test_AreaOfARectangleWithDefaultDimensions(getDefaultRectangleObject):
  assert getDefaultRectangleObject.area() == 50, "Value should be 50"

def test_PerimeterOfARectangleWithDefaultDimensions(getDefaultRectangleObject):
  assert getDefaultRectangleObject.perimeter() == 30, "Value should be 30"


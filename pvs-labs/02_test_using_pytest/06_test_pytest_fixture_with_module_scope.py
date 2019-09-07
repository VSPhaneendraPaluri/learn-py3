'''
This tutorial demonstrates the use of PYTEST fixture highlighting
module scope

NOTE : Try running the tutorial example in verbose mode with arguments --capture=no

NOTE : Concepts that one shall be to appreciate after solving this tutorial
1. What does one need to do in order to have setup called only once per module scope ?

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

@pytest.fixture
def getDefaultRectangleObject():
  print("\nSetUp called ...")
  rectangleObj = None
  return rectangleObj

def test_AreaOfARectangleWithDefaultDimensions(getDefaultRectangleObject):
  assert getDefaultRectangleObject.area() == 50, "Value should be 50"

def test_PerimeterOfARectangleWithDefaultDimensions(getDefaultRectangleObject):
  assert getDefaultRectangleObject.perimeter() == 30, "Value should be 30"


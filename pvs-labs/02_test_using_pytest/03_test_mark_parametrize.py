'''
This tutorial demonstrates the use of test mark decorators 'paarametrize' in enabling
test parameterization for PYTEST

Run the parametrized tests by running
  >$ pytest <filename.py> -v

  Inputs:
    -----------------------------------
    Length | Breadth | Area | Perimeter
    -----------------------------------
       1   |    2    |   2  |     6
      13   |   12    |  156 |    50
      10   |   20    |  200 |    60
    -----------------------------------

NOTE : Concepts that one shall be to appreciate after solving this tutorial
  1. Test parametrization of a fixture with a known/golden test vector
  2. Use of 'parametrize' mark decorator

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

def test_AreaOfARectangleWithTestVectors():
  rectangle = Rectangle()
  assert rectangle.area() == 0
  assert rectangle.perimeter() == 0


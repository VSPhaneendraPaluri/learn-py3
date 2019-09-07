'''
This tutorial demonstrates the user of asserts made available for PYTEST

The users could easily appreciate the user of PYTEST for testing one's Python code

Observations:
1. No specific Assertxxxx to be remembered or used
2. It's simple assert statement that PYTEST uses.  Behind the scenes, Python rewrites the asserts

NOTE:
Question: How would you add custom assertions ?
Answer  : By using 'pytest_assertrepr_compare' hook


'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from square import Square

import pytest

def test_AreaOfASqaureWithDefaultSide():
  square = Square()  
  assert False

def test_AreaOfASquareWithNonDefaultSide():
  square = Square()
  assert False, "Value should be 100"

def test_PerimeterOfASquareWithNonDefaultSide():
  square = Square()
  assert False, "Perimeter is 4*side = 60"

'''
This tutorial demonstrates the use of classical xUnit-style fixtures
at the module level

This demonstrates that PYTEST continues to support the xUnit-style fixtures

NOTE :  Try running the tutorial example in verbose mode with arguments --capture=no

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

rectangle = None

## User may try setup_module() v/s setup_module(module)
def setup_module(module):
  print("\nsetup_module called ...")
  global rectangle
  rectangle = Rectangle()

def teardown_module(module):
  print("\nteardown_module called ...")

def test_AreaOfARectangleWithDefaultDimensions():
  assert rectangle.area() == 50, "Value should be 50"

def test_PerimeterOfARectangleWithDefaultDimensions():
  assert rectangle.perimeter() == 30, "Value should be 30"


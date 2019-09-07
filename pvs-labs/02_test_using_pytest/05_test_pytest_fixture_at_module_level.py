'''
This tutorial demonstrates the use of PYTEST fixtures at the module level

Use the fixtures to setup and teardown at the module level

NOTE : Try running the tutorial example in verbose mode with arguments --capture=no

NOTE : Concepts that one shall be to appreciate after solving this tutorial
  1. Isn't this similar to 'Dependency Injection' ?
  2. Did one notice how fixtures are passed to the test functions ?
  3. What did one observe in the run log ?
  4. How can one control setup and teardown per session instead of module ?
  5. How does one eliminate use of global variables within the files ?
  6. How does one write a function in the same module that doesn't use same setup/teardown ?

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

rectangle = None

def test_AreaOfARectangleWithDefaultDimensions():
  assert rectangle.area() == 50, "Value should be 50"

def test_PerimeterOfARectangleWithDefaultDimensions():
  assert rectangle.perimeter() == 30, "Value should be 30"

'''
This tutorial demonstrates the use of test markers made available for PYTEST

The users could easily appreciate the user of markers that enable users to filter tests
based upon the markers

Exercise the following :
  Use the switch -rxs to display the reason for the skipped tests
  Eg. >$ pytest <filename.py> -rxs -v

  Expectation:
  1. 'test_AreaOfARectangleWithLength5AndBreadth10' test should not execute
  2. 'test_CheckForPythonVersion' test should get executed, only conditionally though !

NOTE : Concepts that one shall be to appreciate after solving this tutorial
  1. Use of Skip, SkipIf mark decorators in order to group tests

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

def test_AreaOfARectangleWithLength5AndBreadth10():
  rectangle = Rectangle(5, 10)
  assert rectangle.area() == 50, "Value should be 50"

def test_CheckForPythonVersion():
  rectangle = Rectangle()
  assert rectangle.area() == 50, "Value should be 50"


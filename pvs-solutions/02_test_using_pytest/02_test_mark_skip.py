'''
This tutorial demonstrates the use of test markers made available for PYTEST

The users could easily appreciate the user of markers that enable users to filter tests
based upon the markers

Exercise the following :
  Use the switch -rxs to display the reason for the skipped tests
  Eg. >$ pytest <filename.py> -rxs -v

'''

import os, sys

packageRelativePath = '..' + os.sep + '..' + os.sep + 'test-objects'
sys.path.insert(0, packageRelativePath)

from rectangle import Rectangle

import pytest

@pytest.mark.skip(reason="Default perimeter is already using length = 5 and breadth = 10")
def test_AreaOfARectangleWithLength5AndBreadth10():
  rectangle = Rectangle(5, 10)
  assert rectangle.area() == 50, "Value should be 50"

@pytest.mark.skipIf(sys.getfilesystemencoding() != "", reason="This tutorial session expects user to have Python 3.7 or higher !")
def test_CheckForPythonVersion():
  rectangle = Rectangle()
  assert rectangle.area() == 50, "Value should be 50"


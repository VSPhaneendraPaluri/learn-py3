'''
This tutorial demonstrates the use of PYTEST fixtures at the module level

NOTE : Try running the tutorial example in verbose mode with arguments --capture=no

NOTE : What do you observe ?
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

# FIXTURE USE
# NOTE:  Both signatures 1 & 2 are valid, and equivalent
# 1. @pytest.fixture
# 2. @pytest.fixture(scope="module")
@pytest.fixture
def pytestSetUp(scope="module"):
  print("\npytestSetUp called ...")
  global rectangle
  rectangle = Rectangle()

@pytest.fixture(scope="module")
def pytestTearDown():
  print("\npytestTearDown called ...")

def test_AreaOfARectangleWithDefaultDimensions(pytestSetUp, pytestTearDown):
  assert rectangle.area() == 50, "Value should be 50"

def test_PerimeterOfARectangleWithDefaultDimensions(pytestSetUp, pytestTearDown):
  assert rectangle.perimeter() == 30, "Value should be 30"

'''
  This tutorial session help user in starting off with OOPs in Python.

  The below automated test shall help user create a class in new-style

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

class TestClass(object):
  '''
  >>> testClassObject = TestClass()
  
    This automated test shall help user create a user function with
    his choice of arguments
  >>> testClassObject.findMaximumValue(10, 12, 14, 20, 18, 16)
  20

    This automated test shall help user create a user function with
    a single argument taking in a list (or set, tuple, etc.)
  >>> testClassObject.findMinimumValueinAList([1, 10, 5, 3])
  1

  '''
  pass
  

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

'''
  This tutorial session help user in starting off with OOPs in Python.

  The below automated test shall help user create a class in new-style

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

class TestClass(object):
  '''  
    This automated test shall help user create local (private) variables
    and lets manupulate input values
  >>> testClassObject = TestClass([1, 5, 3])
  >>> testClassObject.computeSquaresOfInputArguments()
  >>> testClassObject.substractOriginalListfromSquareList()
  >>> testClassObject.printResultantList()
  [0, 20, 6]

  '''
  pass
  

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

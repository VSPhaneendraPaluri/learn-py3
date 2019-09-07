'''
  This tutorial session help user in starting off with OOPs in Python.

  The below automated test shall help user create a class in new-style

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

class TestClassWithDefaultConstructor(object):
  '''
  >>> testClassObject = TestClassWithDefaultConstructor()
  This print statement is output by the default constructor

  '''
  def __init__(self):
    print('This print statement is output by the default constructor')


class TestClassWithParameterizedConstructor(object):
  '''
  NOTE: While completing this exercise, users may even refer to tutorial session #5
        mentioning generic function creation

  >>> testClassObject = TestClassWithParameterizedConstructor('This constructor takes in arguments')
  This print statement is output by the parameterized constructor
  Input Argument : This constructor takes in arguments

  '''
  def __init__(self, inputString):
    print('This print statement is output by the parameterized constructor')
    print('Input Argument : {}'.format(inputString))


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

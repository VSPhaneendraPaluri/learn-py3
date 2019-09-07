'''
  This tutorial session help user in starting off with OOPs in Python.

  The below automated test shall help user create a class in new-style

'''

# DO NOT MODIFY THIS !
class BaseClass(object):

  def __init__(self):
    print('Base Class Constructor called ...')
  
  def firstFunction(self):
    print('Base Class - firstFunction called ...')
  
  def secondFunction(self):
    print('Base Class - secondFunction called ...')


# Start writing up the new code from here
# Start fixing up the broken code from here

class DerivedClass(BaseClass):
  '''
  The following automated tests shall help users fix the derived class
  and help in understanding inheritance concepts in Python

  >>> baseClassObject = BaseClass()
  Base Class Constructor called ...

  NOTE : Try for multiple variations for achieving this
  >>> derivedClassObject = DerivedClass()
  Base Class Constructor called ...
  Derived Class Constructor called ...
  
  >>> baseClassObject.firstFunction()
  Base Class - firstFunction called ...

  >>> derivedClassObject.firstFunction()
  Derived Class - firstFunction called ...

  >>> baseClassObject.secondFunction()
  Base Class - secondFunction called ...

  >>> derivedClassObject.secondFunction()
  Base Class - secondFunction called ...

  '''
  def __init__(self):
    super().__init__()
    print('Derived Class Constructor called ...')
  
  def firstFunction(self):
    print('Derived Class - firstFunction called ...')


class NewDerivedClass(BaseClass):
  '''
  The following automated tests shall help users fix the derived class
  and help in understanding inheritance concepts in Python
  
  >>> newDerivedClassObject = NewDerivedClass()
  Base Class Constructor called ...
  '''
  pass


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

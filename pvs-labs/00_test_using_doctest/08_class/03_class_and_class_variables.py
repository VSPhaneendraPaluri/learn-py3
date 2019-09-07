'''
  This tutorial session help user in starting off with OOPs in Python.

  The below automated test shall help user create a class in new-style

'''

# DO NOT MODIFY THIS FUNCTION !
def compareLists(list1, list2):
  if (list1 == list2):
    return True
  else:
    return False


# Start writing up the new code from here
# Start fixing up the broken code from here

class TestClass(object):
  '''
    This automated test shall illustrate user create class variables
  >>> testClassObject = TestClass()  
  >>> testClassObject.enterVowelsList(['a', 'e', 'i', 'o', 'u'])
  >>> compareLists(testClassObject.getListOfVowels(), testClassObject.vowelsList)
  True

  '''
  pass


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

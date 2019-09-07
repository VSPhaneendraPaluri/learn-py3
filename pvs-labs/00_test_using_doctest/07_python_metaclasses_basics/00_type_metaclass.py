'''
  This tutorial session might not be necessary but my help in knowing the
  right tools that might be required while programming in Python
  
  NOTE :
  1. Everything in Python is an object.
  2. Every class in Python 3 is an instance of 'type' metaclass

  The below automated test shall demo the type of a Python integer
>>> type(integerObject)
<class 'int'>

  The below automated test shall demo the type of a Python string
>>> type(stringObject)
<class 'str'>

  The below automated test shall demo the type of a Python list
>>> type(listObject)
<class 'list'>

  The below automated test shall demo the type of a Python tuple
>>> type(tupleObject)
<class 'tuple'>

  The below automated test shall demo the type of a Python set
>>> type(setObject)
<class 'set'>

  The below automated test shall demo the type of a Python dictionary
>>> type(dictObject)
<class 'dict'>

  The below automated test shall demo the type of a Python function object
>>> type(functionObject)
<class 'function'>

  The below automated test shall help user create a class in new-style
  and print out the type of the class
  (New-Style class is supported from Python v2.1 onwards ?)
>>> type(NewStyleClass)
<class 'type'>

  The below automated test shall help user demo the type of the instance of the class
>>> type(newStyleClassObject)
<class '__main__.NewStyleClass'>

'''

# Start writing up the new code from here
# Start fixing up the broken code from here

integerObject = None
stringObject = None
listObject = None
tupleObject = None
setObject = None
dictObject = None
functionObject = None
NewStyleClass = None
newStyleClassObject = None

# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

'''
  This file lists tests demonstrating copyable attributes of Python Tuples

  NOTE :  This tutorial would also help user in understanding fairly about the
  'copy' Python module
    
>>> originalTuple
(1, [2, 22, 222], (3, 33, 333))

>>> copyByRefTuple
(1, [2, 22, 222], (3, 33, 333))

  The below set of automated tests shall enable the user to understand copy
  by reference attributes of Python Tuple(s)
>>> isEqual(originalTuple, copyByRefTuple)
True
>>> isEqual(originalTuple[1], copyByRefTuple[1])
True
>>> isEqual(originalTuple[2], copyByRefTuple[2])
True

  The below set of automated tests shall enable the user to understand SHALLOW
  COPY nature of Python Tuple(s)
>>> isEqual(originalTuple, shallowCopiedTuple)
True
>>> isEqual(originalTuple[1], shallowCopiedTuple[1])
True
>>> isEqual(originalTuple[2], shallowCopiedTuple[2])
True

  The below set of automated tests shall enable the user to understand DEEP
  COPY nature of Python Tuple(s)
>>> isEqual(originalTuple, deepCopiedTuple)
True
>>> isEqual(originalTuple[1], deepCopiedTuple[1])
True
>>> isEqual(originalTuple[2], deepCopiedTuple[2])
True

'''

## Import libraries here
import sys
import copy


# Helper Function - Need not EDIT this !
def isEqual(arg1, arg2):
  return (arg1 == arg2)

def isNotEqual(arg1, arg2):
  return (arg1 != arg2)


# Start writing up the new code from here
# Start fixing up the broken code from here
originalTuple = ()
copyByRefTuple = ()
shallowCopiedTuple = ()
deepCopiedTuple = ()


# NOTE : Once all the above errors are resolved, uncomment the below assertions
#        DO NOT EDIT THESE ASSERTIONS !
#assert id(originalTuple) == id(copyByRefTuple), "id(originalTuple) and id(copyByRefTuple) should match !"
#assert id(originalTuple[1]) == id(copyByRefTuple[1]), "id(originalTuple[1]) and id(copyByRefTuple[1]) should match !"
#assert id(originalTuple[2]) == id(copyByRefTuple[2]), "id(originalTuple[2]) and id(copyByRefTuple[2]) should match !"

#assert id(originalTuple) == id(shallowCopiedTuple), "id(originalTuple) and id(shallowCopiedTuple) shouldn't match !"
#assert id(originalTuple[1]) == id(shallowCopiedTuple[1]), "id(originalTuple[1]) and id(shallowCopiedTuple[1]) should match !"
#assert id(originalTuple[2]) == id(shallowCopiedTuple[2]), "id(originalTuple[2]) and id(shallowCopiedTuple[2]) should match !"

#assert id(originalTuple) == id(deepCopiedTuple), "id(originalTuple) and id(deepCopiedTuple) shouldn't match !"
#assert id(originalTuple[1]) == id(deepCopiedTuple[1]), "id(originalTuple[1]) and id(deepCopiedTuple[1]) should match !"
#assert id(originalTuple[2]) == id(deepCopiedTuple[2]), "id(originalTuple[2]) and id(deepCopiedTuple[2]) should match !"


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

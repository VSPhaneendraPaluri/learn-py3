'''
  This file lists tests demonstrating copyable attributes of Python Lists

  NOTE :  This tutorial also would help user understand the usage of 'copy' Python module
    
>>> originalList
[1, [2, 22, 222], (3, 33, 333)]

>>> copyByRefList
[1, [2, 22, 222], (3, 33, 333)]

  These automated tests demonstrate assignment property of Python List(s)
>>> isEqual(id(originalList), id(copyByRefList))
True
>>> isEqual(id(originalList[1]), id(copyByRefList[1]))
True
>>> isEqual(id(originalList[2]), id(copyByRefList[2]))
True

  These automated tests demonstrate SHALLOW COPY of Python List(s)
>>> isNotEqual(id(originalList), id(shallowCopiedList))
True
>>> isEqual(id(originalList[1]), id(shallowCopiedList[1]))
True
>>> isEqual(id(originalList[2]), id(shallowCopiedList[2]))
True

  These automated tests demonstrate DEEP COPY of Python List(s)
>>> isNotEqual(id(originalList), id(deepCopiedList))
True
>>> isNotEqual(id(originalList[1]), id(deepCopiedList[1]))
True
>>> isEqual(id(originalList[2]), id(deepCopiedList[2]))
True

'''

## Import libraries here 
# NOTE : import 'copy' module
import sys
#import copy


# Helper functions - Need Not Edit
def isEqual(arg1, arg2):
  return (arg1 == arg2)

def isNotEqual(arg1, arg2):
  return (arg1 != arg2)


# Start writing up the new code from here
# Start fixing up the broken code from here
originalList = []
copyByRefList = []
shallowCopiedList = []
deepCopiedList = []


# NOTE :  Uncomment the below instructions once all the above errors are resolved

#assert id(originalList) == id(copyByRefList), "id(originalList) and id(copyByRefList) doesn't match !"
#assert id(originalList[1]) == id(copyByRefList[1]), "id(originalList[1]) and id(copyByRefList[1]) doesn't match !"
#assert id(originalList[2]) == id(copyByRefList[2]), "id(originalList[2]) and id(copyByRefList[2]) doesn't match !"

#assert id(originalList) != id(shallowCopiedList), "id(originalList) and id(shallowCopiedList) shouldn't match !"
#assert id(originalList[1]) == id(shallowCopiedList[1]), "id(originalList[1]) and id(shallowCopiedList[1]) should match !"
#assert id(originalList[2]) == id(shallowCopiedList[2]), "id(originalList[2]) and id(shallowCopiedList[2]) should match !"

#assert id(originalList) != id(deepCopiedList), "id(originalList) and id(deepCopiedList) shouldn't match !"
#assert id(originalList[1]) != id(deepCopiedList[1]), "id(originalList[1]) and id(deepCopiedList[1]) shouldn't match !"
#assert id(originalList[2]) == id(deepCopiedList[2]), "id(originalList[2]) and id(deepCopiedList[2]) shouldn't match !"


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)

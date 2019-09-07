'''
  This file lists tests for automated testing of non-homogeneous tuples in Python

  The below automated test teaches how reporting of a non-homogeneous Python tuple looks like
>>> tuple1
(1, 2, 'ab', 'd')

  The below automated test illustrates that a non-homogeneous tuple could contain anything
  NOTE :  Nested lists are a subset of this feature
>>> list2
(5, 6, (1, 2, 'ab', 'd'))

  NOTE :
    Rest all the operations on these tuples are very similar to those present within '02_homogeneous_tuples.py'

'''

## Import libraries here
import sys

# Start writing up the new code from here
# Start fixing up the broken code from here
tuple1 = ()
list2 = ()


# main function - DO NOT EDIT THIS !
if __name__ == "__main__":
  import doctest
  failedTestCount, _ = doctest.testmod()
  if (failedTestCount == 0):
    print("Congratulations !!  All the tests have PASSED within ", __file__)
